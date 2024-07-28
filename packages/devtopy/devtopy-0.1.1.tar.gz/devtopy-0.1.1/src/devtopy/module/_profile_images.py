from typing import Union, TYPE_CHECKING

from ..model import ProfileImage, ErrorResponse
from ..exception import DotDevApiError


if TYPE_CHECKING:
    from .._devtopy import DevTo


class ProfileImages:
    def __init__(self, parent: "DevTo"):
        self.parent = parent

    def get(self, username: str):
        endpoint = self.parent._build_url(f"profile_images/{username}")
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            return ProfileImage(**data)
        elif res.status_code == 404:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)
