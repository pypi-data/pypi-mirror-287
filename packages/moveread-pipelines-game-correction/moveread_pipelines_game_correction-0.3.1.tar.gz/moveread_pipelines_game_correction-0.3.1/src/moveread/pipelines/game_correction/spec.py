from typing_extensions import TypedDict
from kv import LocatableKV, KV
from pipeteer import Task
from dslog import Logger
from fastapi import FastAPI
from moveread.pipelines.game_correction import SDK, fastapi, Input, Output, Annotations

class Params(TypedDict):
  logger: Logger
  images: LocatableKV[bytes]
  cache: KV[Annotations]

class GameCorrection(Task[Input, Output, Params, FastAPI]):
  Queues = Task.Queues[Input, Output]
  Params = Params
  Artifacts = FastAPI

  def __init__(self):
    super().__init__(Input, Output)

  def run(self, queues: Queues, params: Params):
    return fastapi(SDK(**queues, cache=params['cache']), logger=params['logger'], images=params['images'])