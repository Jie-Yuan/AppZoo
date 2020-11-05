#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AppZoo.
# @File         : demo
# @Time         : 2020/11/5 8:19 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


from appzoo import App

app = App()
app.add_route('/', lambda **kwargs: "Hello World", method="GET", result_key="keywords")
app.run(port=9955)
