#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : video
# @Time         : 2024/7/26 12:03
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.pipe import *
from meutils.schemas.chatglm_types import VideoRequest, Parameter, VIDEO_BASE_URL, EXAMPLES
from meutils.schemas.task_types import Task

from meutils.decorators.retry import retrying
from meutils.notice.feishu import send_message as _send_message
from meutils.config_utils.lark_utils import get_next_token_for_polling

FEISHU_URL = "https://xchatllm.feishu.cn/sheets/Bmjtst2f6hfMqFttbhLcdfRJnNf?sheet=siLmTk"

send_message = partial(
    _send_message,
    title=__name__,
    url="https://open.feishu.cn/open-apis/bot/v2/hook/dc1eda96-348e-4cb5-9c7c-2d87d584ca18"
)


async def upload(file: bytes, token: Optional[str] = None):
    token = token or await get_next_token_for_polling(FEISHU_URL)

    headers = {
        'Authorization': f'Bearer {token}',
    }

    files = [('file', file)]

    async  with httpx.AsyncClient(base_url=VIDEO_BASE_URL, headers=headers, timeout=60) as client:
        response = await client.post('/static/upload', files=files)

        logger.debug(response.text)
        logger.debug(response.status_code)

        if response.is_success:
            data = response.json()
            return data

        response.raise_for_status()


@retrying(max_retries=8, max=8, predicate=lambda r: r is True)
async def create_task(request: VideoRequest, token: Optional[str] = None):
    token = token or await get_next_token_for_polling(FEISHU_URL)

    headers = {
        'Authorization': f'Bearer {token}',
    }
    payload = request.model_dump()
    async  with httpx.AsyncClient(base_url=VIDEO_BASE_URL, headers=headers, timeout=30) as client:
        response = await client.post('/chat', json=payload)

        logger.debug(response.text)
        logger.debug(response.status_code)

        if response.is_success:
            data = response.json()

            if any(i in str(data) for i in {"您有任务正在排队生成，请稍后再试", }):  # 重试
                return True

            return Task(id=data['result']['chat_id'], data=data, system_fingerprint=token)


async def get_task(task_id: str, token: str):
    task_id = isinstance(task_id, str) and task_id.split("-", 1)[-1]

    headers = {
        'Authorization': f'Bearer {token}',
    }
    async with httpx.AsyncClient(base_url=VIDEO_BASE_URL, headers=headers, timeout=30) as client:
        response = await client.get(f"/chat/status/{task_id}")

        logger.debug(response.text)
        logger.debug(response.status_code)

        if response.is_success:
            data = response.json()
            return data

        response.raise_for_status()


async def composite_video(task_id: str, token: str = None):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    payload = {
        "chat_id": task_id,
        "key": "quiet",
        "audio_id": "669b799d7a9ebbe698de2102"
    }
    # 669b790d7a9ebbe698de20f6 回忆老照片 todo:
    # {chat_id: "66a325cbf66684c40b362a30", key: "epic", audio_id: "669b809d3915c1ddbb3d6705"} 灵感迸发

    async with httpx.AsyncClient(base_url=VIDEO_BASE_URL, headers=headers) as client:
        response = await client.post('/static/composite_video', json=payload)

        logger.debug(response.text)
        logger.debug(response.status_code)

        if response.is_success:
            data = response.json()
            return data
        response.raise_for_status()


if __name__ == '__main__':
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzNmE4NmM1Yzc2Y2Q0MTcyYTE5NGYxMjQwZTgyMmIwOSIsImV4cCI6MTcyMjA1MjU0MSwibmJmIjoxNzIxOTY2MTQxLCJpYXQiOjE3MjE5NjYxNDEsImp0aSI6IjBhZmY5ODljZDJkODQ4Yzg5NDdiZTZhNDkzYjdlOTZlIiwidWlkIjoiNjQ0YTNkMGNiYTI1ODVlOTA0NjAzOWRiIiwidHlwZSI6ImFjY2VzcyJ9.E2oXHnmLV0feDEplVWHJPo_gcbR7DNEc1zAJ7UlRL_4"
    # request = VideoRequest(**EXAMPLES[0])
    # arun(create_task(request))

    request = VideoRequest(**EXAMPLES[1])
    arun(create_task(request))

    # arun(get_task('66a325cbf66684c40b362a30', token))
    # file = Path("/Users/betterme/PycharmProjects/AI/x.jpg").read_bytes()
    # arun(upload(file, token))
