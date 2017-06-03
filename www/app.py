#! C:\python3.6\python.exe
# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from aiohttp import web
from datetime import datetime

def index(request) :
    return web.Response(body='<h1>Awesome</h1>'.encode('utf-8'), content_type='text/html')

@asyncio.coroutine
def init(loop) :
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
