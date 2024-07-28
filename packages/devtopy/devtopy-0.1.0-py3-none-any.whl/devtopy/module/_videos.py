from typing import Union, TYPE_CHECKING

from ..model import VideoArticle, VideoArticleList
from ..exception import DotDevApiError


if TYPE_CHECKING:
    from .._devtopy import DevTo


class Videos:

    def __init__(self, parent: "DevTo"):
        self.parent = parent

    def get_articles_with_video(self, page: int = 1, per_page: int = 24):
        params = {"page": page, "per_page": per_page}
        endpoint = self.parent._build_url_with_params("videos", params)
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            print(data)
            videos = [VideoArticle(**d) for d in data]
            return VideoArticleList(video_articles=videos)
        raise DotDevApiError(response=res)
