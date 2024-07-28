from typing import Optional, List, Union

from pydantic import BaseModel, HttpUrl, Field


class ErrorResponse(BaseModel):
    error: str
    status: int


class User(BaseModel):
    name: str
    username: str
    twitter_username: Optional[str] = None
    github_username: Optional[str] = None
    user_id: Optional[int] = None
    website_url: Optional[Union[HttpUrl, str]] = None
    profile_image: Optional[str] = None
    profile_image_90: Optional[str] = None


class UserList(BaseModel):
    users: List[User]


class Organization(BaseModel):
    name: str
    username: str
    slug: str
    profile_image: str
    profile_image_90: str


class FlareTag(BaseModel):
    name: str
    bg_color_hes: Optional[str] = None
    text_color_hex: str


class Article(BaseModel):
    type_of: str
    id: int
    title: str
    description: str
    readable_publish_date: Optional[str] = None
    slug: str
    path: str
    url: HttpUrl
    comments_count: int
    public_reactions_count: int
    collection_id: Optional[int] = None
    published_timestamp: Optional[str] = Field(default=None)
    positive_reactions_count: int
    cover_image: Optional[HttpUrl] = None
    social_image: HttpUrl
    canonical_url: HttpUrl
    created_at: str
    edited_at: Optional[str] = None
    crossposted_at: Optional[str] = None
    published_at: Optional[str] = None
    last_comment_at: str
    reading_time_minutes: int
    tag_list: str
    tags: List[str]
    body_html: str
    body_markdown: str
    user: User
    organization: Optional[Organization] = None
    flare_tag: Optional[FlareTag] = None


class PublishedArticle(BaseModel):
    type_of: str
    id: int
    title: str
    description: str
    readable_publish_date: Optional[str] = None
    slug: str
    path: str
    url: HttpUrl
    comments_count: int
    public_reactions_count: int
    collection_id: Optional[int] = None
    published_timestamp: str
    positive_reactions_count: int
    cover_image: Optional[HttpUrl] = None
    social_image: Optional[HttpUrl] = None
    canonical_url: HttpUrl
    created_at: Optional[str] = None
    edited_at: Optional[str] = None
    crossposted_at: Optional[str] = None
    published_at: Optional[str] = None
    last_comment_at: Optional[str] = None
    reading_time_minutes: int
    tag_list: List[str]
    tags: Optional[str] = None
    user: User
    organization: Optional[Organization] = None
    flare_tag: Optional[FlareTag] = None


class PublishedArticleList(BaseModel):
    articles: List[PublishedArticle]


class Comment(BaseModel):
    type_of: str = Field(..., description="Type of the comment")
    id_code: str = Field(..., description="Unique identifier for the comment")
    created_at: str = Field(..., description="Creation timestamp of the comment")
    body_html: str = Field(..., description="HTML content of the comment")
    user: User
    children: List["Comment"] = Field(
        default_factory=list, description="Nested replies to this comment"
    )


class CommentList(BaseModel):
    comments: List[Comment]


class FollowedTag(BaseModel):
    id: int
    name: str
    points: float


class FollowedTagList(BaseModel):
    tags: List[FollowedTag]


class Tag(BaseModel):
    id: int
    name: str
    bg_color_hex: Optional[str] = None
    text_color_hex: Optional[str] = None


class TagList(BaseModel):
    tags: List[Tag]


class Organization(BaseModel):
    type_of: str
    id: int
    username: str
    name: str
    summary: Optional[str] = None
    twitter_username: Optional[str] = None
    github_username: Optional[str] = None
    url: Optional[Union[HttpUrl, str]] = None
    location: Optional[str] = None
    tech_stack: Optional[str] = None
    tag_line: Optional[str] = None
    story: Optional[str] = None
    joined_at: Optional[str] = None
    profile_image: Optional[str] = None


class Podcast(BaseModel):
    title: str
    slug: str
    image_url: Optional[Union[str, HttpUrl]] = None


class PodcastEpisode(BaseModel):
    type_of: str
    class_name: str
    id: int
    path: str
    title: str
    image_url: Optional[str] = None
    podcast: Podcast


class PodcastEpisodeList(BaseModel):
    podcast_episodes: List[PodcastEpisode]


class ProfileImage(BaseModel):
    type_of: str
    image_of: str
    profile_image: Optional[Union[str, HttpUrl]] = None
    profile_image_90: Optional[Union[str, HttpUrl]] = None


class Reaction(BaseModel):
    result: str
    category: str
    id: int
    reactable_id: int
    reactable_type: str


class VideoArticleUser(BaseModel):
    name: str


class VideoArticle(BaseModel):
    type_of: str
    id: int
    path: Optional[str] = None
    cloudinary_video_url: Optional[str] = None
    title: str
    user_id: int
    video_duration_in_minutes: str
    video_source_url: HttpUrl
    user: VideoArticleUser


class VideoArticleList(BaseModel):
    video_articles: List[VideoArticle]
