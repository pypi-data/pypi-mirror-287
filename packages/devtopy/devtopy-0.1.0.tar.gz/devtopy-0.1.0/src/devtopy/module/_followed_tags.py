from typing import Union, TYPE_CHECKING

from ..model import FollowedTag, FollowedTagList, ErrorResponse
from ..exception import DotDevApiError


if TYPE_CHECKING:
    from .._devtopy import DevTo


class FollowedTags:

    def __init__(self, parent: "DevTo"):
        self.parent = parent

    def get(self) -> Union[FollowedTagList, ErrorResponse]:
        endpoint = self.parent._build_url("follows/tags")
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            tags = [FollowedTag(**tag) for tag in data]
            return FollowedTagList(tags=tags)
        elif res.status_code == 401:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)
