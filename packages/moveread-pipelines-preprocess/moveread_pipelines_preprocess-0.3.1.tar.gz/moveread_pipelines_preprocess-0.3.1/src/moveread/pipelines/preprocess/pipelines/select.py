from typing import Literal, Any
from dataclasses import dataclass
from haskellian import either as E
from pipeteer import ReadQueue, WriteQueue, Task
from pipeteer.queues import ReadError
import robust_extraction2 as re
from moveread.core import Rectangle

@dataclass
class Input:
  img: str
  model: re.ExtendedModel

@dataclass
class Selected:
  grid_coords: Rectangle
  tag: Literal['selected'] = 'selected'

@dataclass
class Recorrect:
  tag: Literal['recorrect'] = 'recorrect'

Output = Selected | Recorrect

@dataclass
class SelectAPI:

  Qin: ReadQueue[Input]
  Qout: WriteQueue[Output]

  def items(self):
    return self.Qin.items()
  
  @E.do[ReadError]()
  async def select(self, id: str, grid_coords: Rectangle):
    (await self.Qin.read(id)).unsafe()
    (await self.Qout.push(id, Selected(grid_coords=grid_coords))).unsafe()
    (await self.Qin.pop(id)).unsafe()

  @E.do[ReadError]()
  async def recorrect(self, id: str):
    (await self.Qin.read(id)).unsafe()
    (await self.Qout.push(id, Recorrect())).unsafe()
    (await self.Qin.pop(id)).unsafe()

class Select(Task[Input, Output, Any, SelectAPI]):
  
  Queues = Task.Queues[Input, Output]
  Artifacts = SelectAPI

  def __init__(self):
    super().__init__(Input, Output)
  
  def run(self, queues: Task.Queues[Input, Output], params=None) -> SelectAPI:
    return SelectAPI(**queues)