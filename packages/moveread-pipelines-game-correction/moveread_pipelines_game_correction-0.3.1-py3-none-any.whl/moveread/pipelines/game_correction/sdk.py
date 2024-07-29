from typing import Sequence, AsyncIterable, Any
from dataclasses import dataclass
from haskellian import either as E
from kv import KV, ReadError
from pipeteer import ReadQueue, WriteQueue
import sequence_edits as se
import game_prediction2 as gp
from ._types import Annotations, Meta, Input, Output, CorrectResult, BadlyPreprocessed, Item

@dataclass
class SDK:
  Qin: ReadQueue[Input]
  Qout: WriteQueue[Output]
  cache: KV[Annotations]

  def items(self):
    return self.Qin.items().map(lambda e: e.fmap(Meta.of))

  @E.do[ReadError]()
  async def item(self, id: str):
    inp = (await self.Qin.read(id)).unsafe()
    anns = (await self.cache.safe_read(id)).unsafe() or Annotations()
    return Item(title=inp.title, boxes=inp.boxes, anns=anns)
  
  @E.do[ReadError]()
  async def confirm(self, id: str, pgn: Sequence[str], early: bool):
    (await self.Qin.read(id)).unsafe()
    anns = (await self.cache.safe_read(id)).unsafe() or Annotations()
    result = CorrectResult(pgn=pgn, early=early, annotations=anns)
    (await self.Qout.push(id, Output(result))).unsafe()
    (await self.Qin.pop(id)).unsafe()

  @E.do[ReadError]()
  async def repreprocess(self, id: str):
    (await self.Qin.read(id)).unsafe()
    (await self.Qout.push(id, Output(BadlyPreprocessed()))).unsafe()
    (await self.Qin.pop(id)).unsafe()

  async def annotate(self, id: str, anns: Annotations):
    return await self.cache.insert(id, anns)

  @E.do[ReadError]()
  async def predict(self, id: str, *, fen: str | None = None):
    task = (await self.Qin.read(id)).unsafe()
    anns = (await self.cache.safe_read(id)).unsafe() or Annotations()
    preds = task.ocrpreds[:(anns and anns.end_correct)]
    preds = [[p] for p in se.apply(anns.edits or [], list(preds), fill=[('', 0)])]

    return gp.manual_predict(
      preds, manual_ucis=anns and anns.manual_ucis or {},
      annotations=anns and [anns.for_preds()], fen=fen
    )