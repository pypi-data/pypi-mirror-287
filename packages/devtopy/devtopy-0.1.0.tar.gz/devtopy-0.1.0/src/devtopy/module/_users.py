from typing import Optional, Union, TYPE_CHECKING

from ..model import User, UserList, ErrorResponse
from ..exception import DotDevApiError


if TYPE_CHECKING:
    from .._devtopy import DevTo


class Users:

    def __init__(self, parent: "DevTo"):
        self.parent = parent

    def get_organization_users(self, username: str) -> Union[UserList, ErrorResponse]:
        endpoint = self.parent._build_url(f"organizations/{username}/users")
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            users = [User(**u) for u in data]
            return UserList(users=users)
        elif res.status_code == 404:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)

    def get_me(self) -> Union[User, ErrorResponse]:
        endpoint = self.parent._build_url("users/me")
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            return User(**data)
        elif res.status_code == 401:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)

    def invite_user(self, email: str, name: str) -> Optional[ErrorResponse]:
        params = {"email": email, "name": name}
        endpoint = self.parent._build_url("admin/users")
        res = self.parent._request("POST", endpoint, params=params)
        if res.status_code == 200:
            return
        elif res.status_code in (401, 422):
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)
