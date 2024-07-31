#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : vidu_video
# @Time         : 2024/7/31 08:59
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.decorators.retry import retrying
from meutils.pipe import *
from meutils.schemas.vidu_types import BASE_URL, UPLOAD_BASE_URL, ViduRequest, ViduUpscaleRequest
from meutils.schemas.task_types import Task, FileTask

from meutils.notice.feishu import send_message as _send_message
from meutils.config_utils.lark_utils import get_next_token_for_polling

FEISHU_URL = "https://xchatllm.feishu.cn/sheets/Bmjtst2f6hfMqFttbhLcdfRJnNf?sheet=l3VpZf"

send_message = partial(
    _send_message,
    title=__name__,
    url="https://open.feishu.cn/open-apis/bot/v2/hook/dc1eda96-348e-4cb5-9c7c-2d87d584ca18"
)


async def upload(file, token: Optional[str] = None):  # todo: 统一到 file object
    token = token or await get_next_token_for_polling(FEISHU_URL)
    logger.debug(token)

    payload = {"scene": "vidu"}
    headers = {
        "Cookie": token.strip("; Shunt=")  # ;Shunt= 居然失效
    }
    async with httpx.AsyncClient(base_url=UPLOAD_BASE_URL, headers=headers, timeout=60) as client:
        response = await client.post("/files/uploads", json=payload)
        if response.is_success:
            logger.debug(response.json())
            file_id = response.json()['id']
            put_url = response.json()['put_url']  # 图片url

            response = await client.put(put_url, content=file)

            payload = {"id": file_id, "etag": "etag"}
            response = await client.put(f"/files/uploads/{file_id}/finish", json=payload)
            logger.debug(response.text)
            logger.debug(response.status_code)
            logger.debug(put_url.split('?')[0])
            if response.is_success:
                uri = f"ssupload:?id={file_id}"
                return FileTask(id=file_id, url=uri, system_fingerprint=token)

            response.raise_for_status()


@retrying(max_retries=8, max=8, predicate=lambda r: r is True)  # 触发重试
async def create_task(request: ViduRequest, token: Optional[str] = None):
    token = token or await get_next_token_for_polling(FEISHU_URL)

    headers = {
        "Cookie": token
    }
    async with httpx.AsyncClient(base_url=BASE_URL, headers=headers, timeout=60) as client:
        response = await client.post("/tasks", json=request.payload)

        if response.status_code in {429}:  # 触发重试
            return True

        if response.is_success:
            data = response.json()
            task_id = f"vidu-{data['id']}"
            return Task(id=task_id, data=data, system_fingerprint=token)
        else:
            return Task(data=response.text, status=0, status_code=response.status_code)


@retrying(max_retries=8, max=8, predicate=lambda r: r is True)  # 触发重试
async def create_task_upscale(request: ViduUpscaleRequest, token: str):
    payload = {
        "input": {
            "creation_id": str(request.creation_id)
        },
        "type": "upscale",
        "settings": {"model": "stable", "duration": 4}
    }
    headers = {
        "Cookie": token
    }
    async with httpx.AsyncClient(base_url=BASE_URL, headers=headers, timeout=60) as client:
        response = await client.post("/tasks", json=payload)

        if response.status_code in {429}:  # 触发重试
            return True

        if response.is_success:
            data = response.json()
            task_id = f"vidu-{data['id']}"
            return Task(id=task_id, data=data, system_fingerprint=token)
        else:
            return Task(data=response.text, status=0, status_code=response.status_code)


async def get_task(task_id: str, token: str):
    task_id = task_id.split("-", 1)[-1]

    headers = {
        "Cookie": token
    }
    async with httpx.AsyncClient(base_url=BASE_URL, headers=headers, timeout=60) as client:
        response = await client.get(f"/tasks/{task_id}")

        if response.is_success:
            data = response.json()
            return data


async def get_credits(token: str):
    headers = {
        "Cookie": token
    }
    async with httpx.AsyncClient(base_url="https://api.vidu.studio/credit/v1", headers=headers, timeout=60) as client:
        response = await client.get(f"/credits/me")

        if response.is_success:
            data = response.json()
            return data


if __name__ == '__main__':
    token = "JWT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM2ODMyODcsImlhdCI6MTcyMjM4NzI4NywiaXNzIjoiaWFtIiwic3ViIjoiMjM2ODMxNTE4NTAwNTI4NyJ9.4_tA-d3LI4ftNPPoAECdREtQIkn0vq95_OC22SHhfqA; Shunt="

    token = '_GRECAPTCHA=09AA5Y-DIgByrKzLaS28RYGtu7pjIHqheXuH6I30X9gCdhdKkZ7hWEmSOk3r7ZoCEsOd3AakViYdtJDx0tUp6PFNI; HMACCOUNT_BFESS=52C289384C2D380F; Hm_lvt_a3c8711bce1795293b1793d35916c067=1722407183; Hm_lpvt_a3c8711bce1795293b1793d35916c067=1722407183; HMACCOUNT=52C289384C2D380F; io=9aquEdnQWD5BZKbhAB7N; JWT=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjM3MDMxOTIsImlhdCI6MTcyMjQwNzE5MiwiaXNzIjoiaWFtIiwic3ViIjoiMjM2ODY0MTMxMDM5Mzg1NCJ9.x9lKwQoMUBpyUgmWjcF44ktw5SOVp4YD8tiypDozpnM; Shunt=; Hm_lvt_a3c8711bce1795293b1793d35916c067=1753943183493|1722407183; shortid=-xpbaqbc0; debug=undefined; _grecaptcha=09AA5Y-DJWAA6_6nCkB9Y7qyXj1ymsIx2Cc5quDHs_NssUDBFH6_tFy0Xd2EasIWd9n_xYmm2cyTZC9UEyMB-wPCz5S0tCoZnkNNIzhQ; VIDU_SELECTED_LOCALE=zh; VIDU_TOUR="v1"'

    # file = Path('/Users/betterme/PycharmProjects/AI/x.jpg').read_bytes()
    # arun(upload(file, token))
    #
    # print(arun(get_next_token_for_polling(FEISHU_URL)) == token)

    # arun(get_task("vidu-2368380300283813", token=token))

    # arun(create_task_upscale())

    arun(get_credits(token))
