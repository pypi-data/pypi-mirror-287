from enum import Enum
from typing import Union, TYPE_CHECKING

from ..model import Reaction, ErrorResponse
from ..exception import DotDevApiError

if TYPE_CHECKING:
    from .._devtopy import DevTo


class ReactionCategory(Enum):
    LIKE = "like"
    UNICORN = "unicorn"
    EXPLODING_HEAD = "exploding_head"
    RAISED_HANDS = "raised_hands"
    FIRE = "fire"


class ReactableType(Enum):
    COMMENT = "Comment"
    ARTICLE = "Article"
    USER = "User"


class Reactions:

    def __init__(self, parent: "DevTo"):
        self.parent = parent

    def toggle(
        self,
        category: ReactionCategory,
        reactable_id: int,
        reactable_type: ReactableType,
    ) -> Union[Reaction, ErrorResponse]:
        params = {
            "category": category.value,
            "reactable_id": reactable_id,
            "reactable_type": reactable_type.value,
        }
        endpoint = self.parent._build_url("reactions/toggle")
        res = self.parent._request("POST", endpoint, params=params)
        if res.status_code == 200:
            data = res.json()
            return Reaction(**data)
        elif res.status_code == 401:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)

    def create(
        self,
        category: ReactionCategory,
        reactable_id: int,
        reactable_type: ReactableType,
    ) -> Union[Reaction, ErrorResponse]:
        params = {
            "category": category.value,
            "reactable_id": reactable_id,
            "reactable_type": reactable_type.value,
        }
        endpoint = self.parent._build_url("reactions")
        res = self.parent._request("POST", endpoint, params=params)
        if res.status_code == 200:
            data = res.json()
            return Reaction(**data)
        elif res.status_code == 401:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)
