import asyncio
from redis.asyncio import Redis
from config import Database
from typing import List, Union

class RedisClient:
    def __init__(self, host: str, port: int, password: str):
        self.db = Redis(host=host, port=port, password=password, ssl=True, decode_responses=True)

    def ensure_str(self, value: Union[str, int]) -> str:
        if isinstance(value, (str, int)):
            return str(value)
        raise ValueError("Invalid input type: value should be str or int")

    async def is_inserted(self, var: Union[str, int], id: Union[str, int]) -> bool:
        try:
            return self.ensure_str(id) in await self.fetch_all(var)
        except Exception as e:
            print(f"Error in is_inserted: {e}")
            return False

    async def insert(self, var: Union[str, int], id: Union[str, int]) -> bool:
        try:
            var_str, id_str = self.ensure_str(var), self.ensure_str(id)
            users = await self.fetch_all(var_str)
            if id_str not in users:
                users.append(id_str)
                await self.db.set(var_str, " ".join(users))
            return True
        except Exception as e:
            print(f"Error in insert: {e}")
            return False

    async def fetch_all(self, var: Union[str, int]) -> List[str]:
        try:
            data = await self.db.get(self.ensure_str(var))
            return data.split() if data else []
        except Exception as e:
            print(f"Error in fetch_all: {e}")
            return []

    async def delete(self, var: Union[str, int], id: Union[str, int]) -> bool:
        try:
            var_str, id_str = self.ensure_str(var), self.ensure_str(id)
            users = await self.fetch_all(var_str)
            if id_str in users:
                users.remove(id_str)
                await self.db.set(var_str, " ".join(users))
            return True
        except Exception as e:
            print(f"Error in delete: {e}")
            return False


db = RedisClient(Database.REDIS_HOST, Database.REDIS_PORT, Database.REDIS_PASSWORD)
