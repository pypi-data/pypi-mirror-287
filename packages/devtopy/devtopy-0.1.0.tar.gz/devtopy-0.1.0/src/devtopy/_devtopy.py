from urllib.parse import urljoin, urlencode
from typing import Any, Dict, List, Optional

import requests

from .module._article import Articles
from .module._users import Users
from .module._comments import Comments
from .module._followed_tags import FollowedTags
from .module._tags import Tags
from .module._organizations import Organizations
from .module._podcast_episodes import PodcastEpisodes
from .module._profile_images import ProfileImages
from .module._reactions import Reactions
from .module._videos import Videos

VERSION = "0.1.0"


class DevTo:
    base = "https://dev.to/api/"

    def __init__(self, api_key: Optional[str] = None, timeout: int = 5):
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()
        self.articles = Articles(self)
        self.users = Users(self)
        self.comments = Comments(self)
        self.followed_tags = FollowedTags(self)
        self.tags = Tags(self)
        self.organizations = Organizations(self)
        self.podcast_episodes = PodcastEpisodes(self)
        self.profile_images = ProfileImages(self)
        self.reactions = Reactions(self)
        self.videos = Videos(self)

    def _fil_none(self, prams: Dict[str, Any]) -> Dict[str, Any]:
        return {k: v for k, v in prams.items() if v is not None}

    def _if_str_then_lower(self, data: Optional[str]):
        return data.lower() if type(data) is str else data

    def _if_list_str_then_join(self, data: Optional[List[str]], sep: str = ","):
        return self._if_str_then_lower(sep.join(data)) if type(data) is list else data

    def _get_headers(self) -> Dict[str, str]:
        return {
            "User-Agent": f"devtopy/{VERSION}",
            "api-key": self.api_key,
        }

    def _build_url(self, path: str) -> str:
        return urljoin(self.base, path)

    def _build_url_with_params(self, endpoint: str, params: Dict[str, str]) -> str:
        url = self._build_url(endpoint)
        param_str = urlencode(params)
        return f"{url}?{param_str}"

    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        return self.session.request(
            method,
            self._build_url(endpoint),
            timeout=self.timeout,
            headers=self._get_headers(),
            **kwargs,
        )
