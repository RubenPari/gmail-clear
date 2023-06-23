import uuid

from google_auth_oauthlib.flow import Flow
from starlette.requests import Request
from starlette.responses import RedirectResponse

from config.settings import settings

flow = Flow.from_client_secrets_file(
    "client_secrets.json",
    scopes=settings.scopes.split(","),
    redirect_uri=settings.redirect_uri,
)


async def login(request: Request):
    # generate random state
    state = str(uuid.uuid4().hex)

    # save state to session
    request.session["state"] = state

    # generate authorization_url with state
    authorization_url, state = flow.authorization_url(
        access_type="offline",
        state=state,
        include_granted_scopes="true",
    )

    # redirect to authorization_url
    return RedirectResponse(authorization_url)


async def callback(request: Request):
    # check if state is valid
    if request.session.get("state") != request.query_params.get("state"):
        return {"message": "invalid state"}

    # fetch token
    try:
        flow.fetch_token(authorization_response=str(request.url))
    except Exception as e:
        return {"message": "failed to fetch token", "error": str(e)}

    # TODO: fix
    # save token to session
    request.session["token"] = flow.credentials.token

    return {"message": "successfully logged in"}


async def logout(request: Request):
    # remove token from session
    request.session.pop("token", None)

    return {"message": "successfully logged out"}
