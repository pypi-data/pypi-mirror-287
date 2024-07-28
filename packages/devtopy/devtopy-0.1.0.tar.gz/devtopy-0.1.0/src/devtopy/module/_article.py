from typing import List, Optional, Union, TYPE_CHECKING

from ..model import Article, ErrorResponse, PublishedArticleList, PublishedArticle
from ..exception import DotDevApiError


if TYPE_CHECKING:
    from .._devtopy import DevTo


class Articles:

    def __init__(self, parent: "DevTo"):
        self.parent = parent

    def publish(
        self,
        title: str,
        body_markdown: str,
        description: str = "",
        tags: List[str] = [],
        published: bool = False,
        series: Optional[str] = None,
        main_image: Optional[str] = None,
        canonical_url: Optional[str] = None,
        organization_id: Optional[int] = None,
    ) -> Union[Article, ErrorResponse]:
        article = {
            "title": title,
            "body_markdown": body_markdown,
            "description": description,
            "tags": self.parent._if_list_str_then_join(tags),
            "published": published,
            "series": series,
            "main_image": main_image,
            "canonical_url": canonical_url,
            "organization_id": organization_id,
        }
        params = {"article": self.parent._fil_none(article)}
        endpoint = self.parent._build_url("articles")
        res = self.parent._request("POST", endpoint, json=params)
        if res.status_code in (401, 422):
            data = res.json()
            return ErrorResponse(**data)
        elif res.status_code == 201:
            data = res.json()
            return Article(**data)
        raise DotDevApiError(response=res)

    def get(
        self,
        page: int,
        per_page: int = 30,
        tag: Optional[str] = None,
        tags: Optional[List[str]] = None,
        tags_exclude: Optional[List[str]] = None,
        username: Optional[str] = None,
        state: Optional[str] = None,
        top: Optional[int] = None,
        collection_id: int = None,
    ) -> Union[PublishedArticleList, ErrorResponse]:
        params = {
            "page": page,
            "per_page": per_page,
            "tag": self.parent._if_str_then_lower(tag),
            "tags": self.parent._if_list_str_then_join(tags),
            "tags_exclude": self.parent._if_list_str_then_join(tags_exclude),
            "username": username,
            "state": state,
            "top": top,
            "collection_id": collection_id,
        }
        endpoint = self.parent._build_url("articles")
        res = self.parent._request("GET", endpoint, params=params)
        if res.status_code == 200:
            data = res.json()
            articles = [PublishedArticle(**a) for a in data]
            return PublishedArticleList(articles=articles)
        raise DotDevApiError(response=res)

    def get_latest_articles(
        self,
        page: int = 1,
        per_page: int = 30,
    ) -> Union[PublishedArticleList, ErrorResponse]:
        params = {
            "page": page,
            "per_page": per_page,
        }
        endpoint = self.parent._build_url_with_params("articles/latest", params)
        res = self.parent._request("GET", endpoint)
        data = res.json()
        articles = [PublishedArticle(**a) for a in data]
        return PublishedArticleList(articles=articles)

    def get_by_id(self, id: int) -> Union[Article, ErrorResponse]:
        endpoint = self.parent._build_url(f"articles/{id}")
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            return Article(**data)
        elif res.status_code == 404:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)

    def update_by_id(
        self,
        id: int,
        title: str,
        body_markdown: str,
        description: str = "",
        tags: List[str] = None,
        published: bool = False,
        series: Optional[str] = None,
        main_image: Optional[str] = None,
        canonical_url: Optional[str] = None,
        organization_id: Optional[int] = None,
    ) -> Union[Article, ErrorResponse]:
        endpoint = self.parent._build_url(f"articles/{id}")
        article = {
            "title": title,
            "body_markdown": body_markdown,
            "description": description,
            "tags": self.parent._if_list_str_then_join(tags),
            "published": published,
            "series": series,
            "main_image": main_image,
            "canonical_url": canonical_url,
            "organization_id": organization_id,
        }
        params = {"article": self.parent._fil_none(article)}
        res = self.parent._request("PUT", endpoint, json=params)
        if res.status_code == 200:
            data = res.json()
            return Article(**data)
        elif res.status_code in (401, 404, 422):
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)

    def get_article_by_path(self, username: str, slug: str):
        endpoint = self.parent._build_url(f"articles/{username}/{slug}")
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            return Article(**data)
        elif res.status_code == 404:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)

    def get_my_articles(
        self,
        page: int = 1,
        per_page: int = 30,
    ) -> Union[PublishedArticleList, ErrorResponse]:
        params = {"page": page, "per_page": per_page}
        endpoint = self.parent._build_url_with_params("articles/me", params)
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            articles = [PublishedArticle(**a) for a in data]
            return PublishedArticleList(articles=articles)
        elif res.status_code == 404:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)

    def get_my_published_articles(
        self, page: int = 1, per_page: int = 30
    ) -> Union[PublishedArticleList, ErrorResponse]:
        params = {"page": page, "per_page": per_page}
        endpoint = self.parent._build_url_with_params("articles/me/published", params)
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            articles = [PublishedArticle(**a) for a in data]
            return PublishedArticleList(articles=articles)
        elif res.status_code == 401:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)

    def get_my_unpublished_articles(
        self, page: int = 1, per_page: int = 30
    ) -> Union[PublishedArticleList, ErrorResponse]:
        params = {"page": page, "per_page": per_page}
        endpoint = self.parent._build_url_with_params("articles/me/unpublished", params)
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            articles = [PublishedArticle(**a) for a in data]
            return PublishedArticleList(articles=articles)
        elif res.status_code == 401:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)

    def get_all_my_articles(
        self, page: int = 1, per_page: int = 30
    ) -> Union[PublishedArticleList, ErrorResponse]:
        params = {"page": page, "per_page": per_page}
        endpoint = self.parent._build_url_with_params("articles/me/all", params)
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            articles = [PublishedArticle(**a) for a in data]
            return PublishedArticleList(articles=articles)
        elif res.status_code == 401:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)

    # Unpublish

    def get_organization_articles(
        self, username: str
    ) -> Union[PublishedArticleList, ErrorResponse]:
        endpoint = self.parent._build_url(f"organizations/{username}/articles")
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            articles = [PublishedArticle(**a) for a in data]
            return PublishedArticleList(articles=articles)
        elif res.status_code == 404:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)

    # Article with a video
