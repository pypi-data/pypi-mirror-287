from dataclasses import dataclass
from haskellian import either as E
from kv import KV

@dataclass
class Locks:
  kv: KV[bytes]

  @E.do()
  async def acquire(self, id: str) -> bool:
    if (await self.kv.has(id)).unsafe():
      return False
    (await self.kv.insert(id, b'')).unsafe()
    return True
  
  async def locked(self, id: str):
    return await self.kv.has(id)
  
  async def release(self, id: str):
    return await self.kv.delete(id)

  async def clear(self):
    return await self.kv.clear()

  @E.do()
  async def all(self):
    return set(await self.kv.keys().map(E.unsafe).sync())