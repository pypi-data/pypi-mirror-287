import asyncio

from .api_helper import ApiHelper
from .check import check_params
from .exceptions import Timeout

_DEFAULT_RETRIES = 60
_DEFAULT_INTERVAL = 1


class PyCapsolver(ApiHelper):
    def __init__(self, key: str, api_base: str = "https://api.capsolver.com"):
        super().__init__(key, api_base)

    async def create_task(self, task: dict) -> dict:
        return await self.post("/createTask", json_data={"task": task})

    async def get_task_result(self, task_id: str) -> dict:
        return await self.post(f"/getTaskResult", json_data={"taskId": task_id})

    async def get_balance(self) -> dict:
        response = await self.post("/getBalance")
        return response["balance"]

    async def solve(self, task: dict, retries: int = _DEFAULT_RETRIES, interval: int = _DEFAULT_INTERVAL) -> dict:
        check_params(task)

        response = await self.create_task(task)
        if response["status"] == "ready":
            return response["solution"]
        else:
            for _ in range(retries):
                await asyncio.sleep(interval)
                task_result = await self.get_task_result(response["taskId"])
                if task_result["status"] == "processing":
                    continue
                else:
                    return task_result["solution"]
            else:
                raise Timeout("Solving task timed out")
