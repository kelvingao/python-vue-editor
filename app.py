# app.py

# aiohttp imports
from aiohttp import web
import aiohttp_cors

import runcode

default_py_code = """import sys
import os

if __name__ == "__main__":
    print("Hello Python World!!")
"""


# get default code
async def handle_get(request) -> web.json_response:
    code = default_py_code

    output = 'No result!'
    compil = "No compilation for Python"

    resp = dict()
    resp['code'] = code
    resp['output'] = output
    resp['compil'] = compil

    return web.json_response(resp)


# post new code
async def handle_post(request) -> web.json_response:
    code = await request.text()

    run = runcode.RunPyCode(code)
    compil, output = run.run_py_code()
    if not output:
        output = 'No result!'

    resp = dict()
    resp['output'] = output
    resp['compil'] = compil

    return web.json_response(resp)


async def init_app() -> web.Application:
    # instantiate a web app
    app = web.Application()

    # set up routes
    add_route = app.router.add_route
    add_route("GET", "/", handle_get)
    add_route("POST", "/runpy", handle_post)

    # configure default CORS settings
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    # configure CORS on all routes
    for route in list(app.router.routes()):
        cors.add(route)

    return app

if __name__ == '__main__':

    app = init_app()
    web.run_app(app, port=5000)
