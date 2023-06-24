from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


# Check if user is authenticated
class CheckAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        if not request.session.get("token") or request.session.get("token") == "":
            return {"message": "unauthorized"}

        return response
