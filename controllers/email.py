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

    if not id_email:
        return {"message": "id is required"}

    # delete email
    try:
        service.users().messages().delete(userId="me", id=id_email).execute()
    except Exception as e:
        return {"message": "failed to delete email", "error": str(e)}

    return {"message": "successfully deleted email"}


# Delete all emails from latest to numer N
# (N is a number of emails to delete)
async def delete_latest(request: Request):
    # get token from session
    token: str = request.session.get("token")

    # create gmail service
    service = build("gmail", "v1", credentials=Credentials(token=token))

    # get number of emails to delete
    number_of_emails: int = int(request.path_params.get("number_of_emails"))

    if number_of_emails < 1:
        return {"message": "number of emails must be greater than 0"}

    # get emails
    try:
        emails = service.users().messages().list(userId="me").execute()
    except Exception as e:
        return {"message": "failed to get emails", "error": str(e)}

    # delete emails
    for i in range(number_of_emails):
        try:
            service.users().messages().delete(userId="me", id=emails["messages"][i]["id"]).execute()
        except Exception as e:
            return {"message": "failed to delete email", "error": str(e)}

    return {"message": "successfully deleted emails"}


# Delete all emails from range date
async def delete_range(request: Request):
    # get token from session
    token: str = request.session.get("token")

    # create gmail service
    service = build("gmail", "v1", credentials=Credentials(token=token))

    # get date start from query
    date_start: str = request.path_params.get("date_start")

    # get date end from query
    date_end: str = request.path_params.get("date_end")

    # get emails
    try:
        emails = service.users().messages().list(userId="me").execute()
    except Exception as e:
        return {"message": "failed to get emails", "error": str(e)}

    # delete emails
    for email in emails["messages"]:
        try:
            email = service.users().messages().get(userId="me", id=email["id"]).execute()
        except Exception as e:
            return {"message": "failed to get email", "error": str(e)}

        if date_start <= email["internalDate"] <= date_end:
            try:
                service.users().messages().delete(userId="me", id=email["id"]).execute()
            except Exception as e:
                return {"message": "failed to delete email", "error": str(e)}

    return {"message": "successfully deleted emails"}
