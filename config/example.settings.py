from pydantic import BaseSettings


class Settings(BaseSettings):
    redirect_uri: str = "<your redirect uri>"
    scopes: str = "<your scopes>"


settings = Settings()
