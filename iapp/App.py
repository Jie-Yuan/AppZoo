#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : tql-App.
# @File         : App
# @Time         : 2019-08-08 10:26
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

from sanic import Sanic, response

from collections import OrderedDict
from traceback import format_exc  # https://www.cnblogs.com/klchang/p/4635040.html


# import socket
# socket.SO_REUSEPORT = 15


class App(object):

    def __init__(self, debug=False, workers=1):
        self.app = Sanic("App")
        self.debug = debug
        self.workers = workers

    def run(self, host="0.0.0.0", port=8000):
        self.app.run(host, port, self.debug, worker=self.workers)

    def add_route(self, uri="/test", func=lambda x="test": x, methods="GET", version="0.0.1"):
        handler = self._handler(func, methods, version)

        # self.app.route(uri, frozenset({self.methods}))(self._handler(func, methods, version))
        self.app.add_route(handler, uri, frozenset({methods}))

    def _handler(self, func, methods, version):
        async def handler(request):
            """
            request.json: {'a': 1}
            request.args:  {'a': ['1']}
            """
            input = request.json if methods == 'POST' else request.args
            output = OrderedDict()

            try:
                output['Score'] = func(**input)
            except Exception as error:
                output['Predict Error'] = error
                output['Predict Error Plus'] = format_exc().strip()
                output['Score'] = 0
            finally:
                output['Version'] = version
                if self.debug:
                    output['Request Params'] = input

            return response.json(output)

        return handler


if __name__ == '__main__':
    import jieba

    f = lambda **kwargs: kwargs
    f1 = lambda **kwargs: kwargs['x'] + kwargs['y']
    f2 = lambda x=1, y=1: x - y
    f3 = lambda text='小米是家不错的公司': jieba.lcut(text)

    app = App(debug=True)
    app.add_route("/f1", f1, version="1")
    app.add_route("/f2", f2, version="2")
    app.add_route("/f3", f3, version="3")

    app.run()