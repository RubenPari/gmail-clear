import os
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

from routes.routes import routes

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# Setup session
middleware = [
    Middleware(
        SessionMiddleware,
        secret_key="gfuyierafgyweiugfu<wgbfubweuy",
        same_site="lax",
        max_age=3600,
    ),
]

app = Starlette(routes=routes, middleware=middleware)
