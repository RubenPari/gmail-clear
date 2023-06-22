from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

from routes.routes import routes

# Setup session
middleware = [
    Middleware(
        SessionMiddleware,
        secret_key="gfuyierafgyweiugfu<wgbfubweuy",
    ),
]

app = Starlette(routes=routes, middleware=middleware)
