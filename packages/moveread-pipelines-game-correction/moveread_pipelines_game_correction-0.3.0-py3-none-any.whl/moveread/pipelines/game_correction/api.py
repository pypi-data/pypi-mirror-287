import asyncio
from pydantic import BaseModel
from haskellian import Iter, either as E
from kv import LocatableKV
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from sse_starlette import EventSourceResponse
from dslog import Logger
from dslog.uvicorn import setup_loggers_lifespan, DEFAULT_FORMATTER, ACCESS_FORMATTER
from moveread.pipelines.game_correction import SDK, Streams, Message, \
  Meta, Item, CorrectResult, Annotations, Done, Preds

def fastapi(
  sdk: SDK, images: LocatableKV[bytes], *,
  logger = Logger.click().prefix('[GAME CORRECTION]')
):

  streams = Streams[Message]()
  reqIds: dict[str, str] = {}

  app = FastAPI(
    generate_unique_id_function=lambda route: route.name,
    lifespan=setup_loggers_lifespan(
      access=logger.format(ACCESS_FORMATTER),
      uvicorn=logger.format(DEFAULT_FORMATTER),
    )
  )
  
  @app.get('/items', response_model_exclude_none=True)
  async def get_items() -> list[Meta]:
    all = await sdk.items().sync()
    return Iter(E.filter(all)).sync()
  
  @app.get('/items/{id}', response_model_exclude_none=True)
  async def get_item(id: str, resp: Response) -> Item | None:
    if (item := (await sdk.item(id)).get_or(None)):
      item.boxes = [images.url(box) for box in item.boxes]
      return item
    else:
      resp.status_code = 404

  class ConfirmParams(BaseModel):
    pgn: list[str]
    early: bool
    
  @app.post('/items/{id}/confirm')
  async def confirm(id: str, params: ConfirmParams, resp: Response) -> bool:
    r = await sdk.confirm(id, pgn=params.pgn, early=params.early)
    ok = r.tag == 'right'
    if not ok:
      resp.status_code = 404
    return ok
  
  @app.post('/items/{id}/repreprocess')
  async def repreprocess(id: str, resp: Response) -> bool:
    r = await sdk.repreprocess(id)
    ok = r.tag == 'right'
    if not ok:
      resp.status_code = 404
    return ok
  
  @app.post('/items/{id}/annotate')
  async def annotate(id: str, anns: Annotations, resp: Response) -> bool:
    r = await sdk.annotate(id, anns)
    ok = r.tag == 'right'
    if not ok:
      resp.status_code = 404
    return ok

  @app.post('/items/{id}/predict')
  async def predict(id: str, userId: str, reqId: str, fen: str | None = None) -> list[Preds|Done]:
    e = await sdk.predict(id, fen=fen)
    if e.tag == 'left':
      streams.push(userId, Done(reqId=reqId))
      return JSONResponse(status_code=404, content=e.value) # type: ignore
    
    reqIds[userId] = reqId
    preds = []

    for ps in e.value:
      if reqIds.get(userId) != reqId:
        logger(f'UserID: {userId}, ReqId: {reqId} got canceled.', level='DEBUG')
        return preds
      msg = Preds(reqId=reqId, preds=ps)
      streams.push(userId, msg)
      await asyncio.sleep(0) # yield control to the event loop, to force result streaming
      preds.append(msg)
    
    streams.push(userId, Done(reqId=reqId))
    return preds

  @app.get('/preds/{userId}')
  def preds(userId: str):
    return EventSourceResponse(streams.listen(userId).map(lambda m: m.model_dump_json()))
  
  return app


def clientgen():
  from argparse import ArgumentParser

  parser = ArgumentParser()
  parser.add_argument('-o', '--output', required=True)

  args = parser.parse_args()

  from openapi_ts import generate_client

  schema = fastapi({}, {}).openapi() # type: ignore
  generate_client(schema, args.output)