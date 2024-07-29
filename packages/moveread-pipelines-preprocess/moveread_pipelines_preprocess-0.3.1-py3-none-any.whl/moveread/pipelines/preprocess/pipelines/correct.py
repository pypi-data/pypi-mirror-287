from typing_extensions import Literal, TypedDict
from dataclasses import dataclass
from uuid import uuid4
from haskellian import either as E
from kv import KV
from pipeteer import ReadQueue, WriteQueue, Task
import robust_extraction2 as re
from robust_extraction2 import Corners
import pure_cv as vc
from pure_cv import Rotation
from dslog import Logger

@dataclass
class Input:
  img: str

@dataclass
class Corrected:
  corners: Corners
  corrected: str
  tag: Literal['corrected'] = 'corrected'

@dataclass
class Rotated:
  rotation: Rotation
  rotated: str
  tag: Literal['rotated'] = 'rotated'

Output = Corrected | Rotated

@dataclass
class CorrectAPI:

  Qin: ReadQueue[Input]
  Qout: WriteQueue[Output]
  images: KV[bytes]
  logger: Logger
  
  def items(self):
    return self.Qin.items()
  
  @E.do()
  async def correct(self, id: str, corners: Corners):
    inp = (await self.Qin.read(id)).unsafe()
    mat = vc.decode((await self.images.read(inp.img)).unsafe())
    corr_mat = re.correct_perspective(mat, corners)
    corr_img = vc.encode(corr_mat, '.jpg')
    corr = f'{id}/manually-corrected_{uuid4()}.jpg'
    (await self.images.insert(corr, corr_img)).unsafe()
    self.logger(f'Corrected "{inp.img}" to "{corr}"', level='DEBUG')
    next = Corrected(corners=corners, corrected=corr)
    (await self.Qout.push(id, next)).unsafe()
    (await self.Qin.pop(id)).unsafe()
  
  @E.do()
  async def rotate(self, id: str, rotation: Rotation):
    inp = (await self.Qin.read(id)).unsafe()
    mat = vc.decode((await self.images.read(inp.img)).unsafe())
    rot_img = vc.encode(vc.rotate(mat, rotation), '.jpg')
    rot = f'{id}/rotated_{uuid4()}.jpg'
    (await self.images.insert(rot, rot_img)).unsafe()
    self.logger(f'Rotated "{inp.img}" to "{rot}"', level='DEBUG')
    (await self.Qout.push(id, Rotated(rotation=rotation, rotated=rot))).unsafe()
    (await self.Qin.pop(id)).unsafe()

class Params(TypedDict):
  images: KV[bytes]
  logger: Logger

class Correct(Task[Input, Output, Params, CorrectAPI]):

  Input = Input
  Output = Output
  Queues = Task.Queues[Input, Output]
  Params = Params
  Artifacts = CorrectAPI

  def __init__(self):
    super().__init__(Input, Output) # type: ignore
  
  def run(self, queues: Task.Queues[Input, Corrected | Rotated], params: Params):
    return CorrectAPI(**queues, **params)