from typing import Union, TYPE_CHECKING

from ..model import Tag, TagList, ErrorResponse
from ..exception import DotDevApiError


if TYPE_CHECKING:
    from .._devtopy import DevTo


class Tags:

    def __init__(self, parent: "DevTo"):
        self.parent = parent

    def get(self, page=1, per_page=10) -> Union[TagList, ErrorResponse]:
        params = {"page": page, "per_page": per_page}
        endpoint = self.parent._build_url_with_params("tags", params=params)
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            tags = [Tag(**tag) for tag in data]
            return TagList(tags=tags)
        elif res.status_code == 401:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)
