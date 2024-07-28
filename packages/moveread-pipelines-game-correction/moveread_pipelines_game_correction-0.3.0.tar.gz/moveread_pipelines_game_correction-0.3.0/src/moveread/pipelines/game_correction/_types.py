from typing import Literal, Sequence
from dataclasses import dataclass, field
from pydantic import BaseModel
import sequence_edits as se
from game_prediction2 import Annotations as PredAnnotations, Pred
from chess_notation.language import Language
from chess_notation.styles import PawnCapture, PieceCapture

class Preds(BaseModel):
  reqId: str
  tag: Literal['preds'] = 'preds'
  preds: list[Pred]

class Done(BaseModel):
  reqId: str
  tag: Literal['done'] = 'done'

Message = Preds | Done

NA = Literal['N/A']
def no_na(value):
  if value != 'N/A':
    return value

@dataclass
class Annotations:
  lang: Language | NA | None = None
  pawn_capture: PawnCapture | NA | None = None
  piece_capture: PieceCapture | NA | None = None
  end_correct: int | None = None
  manual_ucis: dict[int, str] = field(default_factory=dict)
  edits: Sequence[se.Edit] = field(default_factory=list)

  def for_preds(self) -> 'PredAnnotations':
    """Convert to `game_correction.Annotations` (replaces `'N/A'`s with `None`s)"""
    return PredAnnotations(
      lang=no_na(self.lang),
      pawn_capture=no_na(self.pawn_capture),
      piece_capture=no_na(self.piece_capture),
    )
  
@dataclass
class Meta:
  title: str
  id: str
  @classmethod
  def of(cls, entry: tuple[str, 'Input']):
    return cls(id=entry[0], title=entry[1].title)

@dataclass(kw_only=True)
class BaseItem:
  title: str
  boxes: Sequence[str]

@dataclass(kw_only=True)
class Input(BaseItem):
  ocrpreds: Sequence[Sequence[tuple[str, float]]]
  """MOVE x TOP_PREDS x (word, logprob)"""

@dataclass
class Item(BaseItem):
  anns: Annotations

@dataclass
class CorrectResult:
  annotations: Annotations
  pgn: Sequence[str]
  early: bool
  tag: Literal['correct'] = field(default='correct', kw_only=True)

@dataclass
class BadlyPreprocessed:
  tag: Literal['badly-preprocessed'] = 'badly-preprocessed'

@dataclass
class Output:
  output: CorrectResult | BadlyPreprocessed
