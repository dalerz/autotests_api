from clients.api_client import ApiClient
from httpx import  Response
from typing import TypedDict

class LogiRequestDict(TypedDict):
    email: str
    password: str

class RefreshRequestDict(TypedDict):
    refreshToken: str
class AuthenticationClient(ApiClient):
    def login_api(self, request: LogiRequestDict) -> Response:
        return self.post("api/v1/authentication/login", json=request)

    def refresh_token_api(self, request: RefreshRequestDict) -> Response:
        return self.post("api/v1/authentication/refresh", json=request)
