from datetime import datetime
from typing import List, Optional, Union, TypedDict

from pydantic import BaseModel, Field, HttpUrl


class Bookmark(BaseModel):
    comment: str
    created_datetime: datetime
    created_epoch: int
    user: str
    permalink: HttpUrl
    private: bool
    tags: List[str] = Field(default_factory=list)
    eid: Optional[str] = None
    comment_raw: Optional[str] = None
    favorites: List[dict] = Field(default_factory=list)


class Entry(BaseModel):
    count: int
    is_invalid_url: bool
    has_asin: bool
    smartphone_app_entry_url: str = Field(default="")
    entry_url: HttpUrl
    eid: str
    root_url: HttpUrl
    favicon_url: HttpUrl
    title: str
    title_last_editor: str = Field(default="")
    url: HttpUrl


class NotFoundEntry(BaseModel):
    message: str
    title: str
    favicon_url: HttpUrl
    url: HttpUrl


class UserInfo(BaseModel):
    name: str
    plususer: bool
    private: bool
    is_oauth_twitter: bool
    is_oauth_evernote: bool
    is_oauth_facebook: bool
    is_oauth_mixi_check: bool


class Tag(BaseModel):
    count: int
    tag: str


class Tags(BaseModel):
    tags: List[Tag]


class BookmarkResponse(BaseModel):
    bookmark: Bookmark
    entry: Optional[Union[Entry, NotFoundEntry]] = None
    user: Optional[UserInfo] = None
    tags: Optional[List[Tag]] = None


class FeedEntry(TypedDict):
    id: str
    title: str
    link: str
    summary: str
    updated: str  # ISO 8601形式の日時文字列
    hatena_bookmarkcount: Optional[str]
    hatena_bookmarkcommentlistpageurl: Optional[str]
    hatena_imageurl: Optional[str]
