#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : x
# @Time         : 2024/7/29 09:54
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : 

from meutils.pipe import *
import execjs

js_code = open("app.a2ff1e35.js", "r", encoding="utf-8").read()

# 使用execjs编译JavaScript代码
ctx = execjs.compile(js_code)

# 执行JavaScript函数
result = ctx.call("e")

print(result)  # 输出: Hello, World!