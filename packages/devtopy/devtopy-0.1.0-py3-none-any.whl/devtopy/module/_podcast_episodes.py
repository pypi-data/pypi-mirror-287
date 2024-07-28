from typing import Optional, Union, TYPE_CHECKING

from ..model import PodcastEpisode, PodcastEpisodeList, ErrorResponse
from ..exception import DotDevApiError


if TYPE_CHECKING:
    from .._devtopy import DevTo


class PodcastEpisodes:

    def __init__(self, parent: "DevTo"):
        self.parent = parent

    def get(
        self, username: Optional[str] = None, page: int = 1, per_page: int = 10
    ) -> Union[dict, ErrorResponse]:
        params = {"page": page, "per_page": per_page}
        req_params = self.parent._fil_none(params)
        endpoint = self.parent._build_url_with_params("podcast_episodes", req_params)
        res = self.parent._request("GET", endpoint, params=params)
        if res.status_code == 200:
            data = res.json()
            podcast_episodes = [PodcastEpisode(**a) for a in data]
            return PodcastEpisodeList(podcast_episodes=podcast_episodes)
        elif res.status_code == 404:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)
