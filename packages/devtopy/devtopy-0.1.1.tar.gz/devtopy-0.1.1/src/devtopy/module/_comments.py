from typing import List, Optional, Union, TYPE_CHECKING

from ..model import Comment, CommentList, ErrorResponse
from ..exception import DotDevApiError


if TYPE_CHECKING:
    from .._devtopy import DevTo


class Comments:

    def __init__(self, parent: "DevTo"):
        self.parent = parent

    def get_article_comments(self, a_id: str) -> Union[CommentList, ErrorResponse]:
        params = {"a_id": a_id}
        endpoint = self.parent._build_url_with_params("comments", params=params)
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            comments = [Comment(**comment) for comment in data]
            return CommentList(comments=comments)
        elif res.status_code == 404:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)

    def get_podcast_episode_comments(
        self, p_id: str
    ) -> Union[CommentList, ErrorResponse]:
        params = {"p_id": p_id}
        endpoint = self.parent._build_url_with_params("comments", params=params)
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            comments = [Comment(**comment) for comment in data]
            return CommentList(comments=comments)
        elif res.status_code == 404:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)

    def get_comment_by_id(self, id_code: str) -> Union[Comment, ErrorResponse]:
        endpoint = self.parent._build_url(f"comments/{id_code}")
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            return Comment(**data)
        elif res.status_code == 404:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)
