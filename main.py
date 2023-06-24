import os
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

from middlewares.checkAuth import CheckAuthMiddleware
from routes.routes import routes

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

middleware = [
    Middleware(
        SessionMiddleware,
        secret_key="gfuyierafgyweiugfu<wgbfubweuy",
        same_site="lax",
        max_age=3600,
    ),
    Middleware(
        CheckAuthMiddleware,
        exclude_routes=["/auth/login", "/auth/callback", "/auth/logout"],
    ),
]

app = Starlette(routes=routes, middleware=middleware)
