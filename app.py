# app.py

# aiohttp imports
from aiohttp import web
import aiohttp_cors


# sleight imports
from views import RunPyCode

async def init_app() -> web.Application:
    # instantiate a web app
    app = web.Application()
    
    # instantiate a view
    py_code = RunPyCode()
    
    # set up routes
    add_route = app.router.add_route
    add_route("GET", "/runpy", history.get_symbols)

    
    # configure default CORS settings
    cors = aiohttp_cors.setup(app, defaults = {
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials = True,
            expose_headers = "*",
            allow_headers = "*",
        )
    })

    # configure CORS on all routes
    for route in list(app.router.routes()):
        cors.add(route)

    return app

if __name__ == '__main__':

    app = init_app()

    web.run_app(app, port=5000)
