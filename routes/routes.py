from starlette.routing import Route

from controllers import auth, email

routes = [
    # -------------- Auth --------------
    Route("/auth/login", endpoint=auth.login, methods=["GET"]),
    Route("/auth/callback", endpoint=auth.callback, methods=["GET"]),
    Route("/auth/logout", endpoint=auth.logout, methods=["GET"]),

    # -------------- Email --------------
    Route("/email/{id}", endpoint=email.delete_by_id, methods=["DELETE"]),
    Route("/email/latest/{number_of_emails}", endpoint=email.delete_latest, methods=["DELETE"]),
    Route("/email/by-range", endpoint=email.delete_range, methods=["DELETE"]),
]
