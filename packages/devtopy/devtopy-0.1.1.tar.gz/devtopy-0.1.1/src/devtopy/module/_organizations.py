from typing import Union, TYPE_CHECKING

from ..model import (
    PublishedArticle,
    PublishedArticleList,
    User,
    UserList,
    Organization,
    ErrorResponse,
)
from ..exception import DotDevApiError


if TYPE_CHECKING:
    from .._devtopy import DevTo


class Organizations:
    def __init__(self, parent: "DevTo"):
        self.parent = parent

    def get(self, organization_name: str) -> Union[User, ErrorResponse]:
        endpoint = self.parent._build_url(f"organizations/{organization_name}")
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            return Organization(**data)
        elif res.status_code == 401:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)

    def get_users(self, organization_name: str) -> Union[UserList, ErrorResponse]:
        endpoint = self.parent._build_url(f"organizations/{organization_name}/users")
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            users = [User(**u) for u in data]
            return UserList(users=users)
        elif res.status_code == 404:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)

    def get_articles(
        self, organization_name: str, page: int = 1, per_page: int = 30
    ) -> Union[PublishedArticleList, ErrorResponse]:
        params = {"page": page, "per_page": per_page}
        endpoint = self.parent._build_url_with_params(
            f"organizations/{organization_name}/articles", params
        )
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            articles = [PublishedArticle(**a) for a in data]
            return PublishedArticleList(articles=articles)
        elif res.status_code == 404:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)
