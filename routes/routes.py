from starlette.routing import Route

from controllers import auth

routes = [
    # -------------- Auth --------------
    Route("/auth/login", endpoint=auth.login),
    Route("/auth/callback", endpoint=auth.callback),
    Route("/auth/logout", endpoint=auth.logout),
]
