from google.auth.api_key import Credentials
from googleapiclient.discovery import build
from starlette.requests import Request


# Delete email by id
async def delete_by_id(request: Request):
    # get token from session
    token: str = request.session.get("token")

    # create gmail service
    service = build("gmail", "v1", credentials=Credentials(token=token))

    # get id from path
    id_email: str = request.path_params.get("id")

    # delete email
    try:
        service.users().messages().delete(userId="me", id=id_email).execute()
    except Exception as e:
        return {"message": "failed to delete email", "error": str(e)}

    return {"message": "successfully deleted email"}
