import json
from typing import Any, Dict, List, Optional, Union
from urllib.parse import urljoin, urlencode, quote

import requests


from ._auth import HatenaBookmarkAuth
from .model import Bookmark, Entry, NotFoundEntry, Tags, UserInfo

VERSION = "0.1.0"


class HatenaBookmarkAPIError(Exception):
    pass


class HatenaBookmarkClient:
    base_url = "https://bookmark.hatenaapis.com/"
    ua = {"User-Agent": f"hatebpy/{VERSION}"}

    def __init__(self, auth: HatenaBookmarkAuth):
        self.auth = auth
        self.session = requests.Session()

    def _build_url(self, endpoint: str, base: str = None) -> str:
        return urljoin(base or self.base_url, endpoint)

    def _build_url_with_params(self, endpoint: str, params: Dict[str, str]) -> str:
        url = self._build_url(endpoint)
        param_str = urlencode(params)
        return f"{url}?{param_str}"

    def _get_headers(self, headers: Dict[str, Any] = {}) -> Dict[str, Any]:
        return {**self.ua, **headers}

    def _request(
        self,
        endpoint: str,
        headers: Dict[str, Any] = {},
        method: str = "GET",
        **kwargs,
    ) -> requests.Response:
        r = self.session.request(
            method,
            self._build_url(endpoint),
            auth=self.auth.get_auth_headers(),
            headers=headers,
            **kwargs,
        )
        return r

    def get_bookmark(self, url: str) -> Optional[Bookmark]:
        params = {"url": url}
        endpoint = self._build_url_with_params("rest/1/my/bookmark", params)
        r = self._request(endpoint, headers=self._get_headers())
        if r.status_code == 200:
            bookmark_data = json.loads(r.text)
            return Bookmark(**bookmark_data)
        elif r.status_code == 404:
            return
        elif r.status_code == 403:
            text = f"Permission denied: {r.text}"
            raise HatenaBookmarkAPIError(text)
        raise HatenaBookmarkAPIError(f"Unknown error: [{r.status_code}] {r.text}")

    def update_bookmark(
        self,
        url: str,
        comment: str = "",
        tags: List[str] = [],
        post_twitter: bool = False,
        post_mixi: bool = False,
        post_evernote: bool = False,
        private: bool = False,
    ) -> Bookmark:
        params = {
            "url": url,
            "comment": comment,
            "tags": tags,
            "post_twitter": post_twitter,
            "post_mixi": post_mixi,
            "post_evernote": post_evernote,
            "private": private,
        }
        endpoint = self._build_url_with_params("rest/1/my/bookmark", params)
        r = self._request(endpoint, method="POST", headers=self._get_headers())
        if r.status_code == 200:
            bookmark_data = json.loads(r.text)
            return Bookmark(**bookmark_data)
        elif r.status_code == 404:
            return
        elif r.status_code == 403:
            text = f"Permission denied: {r.text}"
            raise HatenaBookmarkAPIError(text)
        raise HatenaBookmarkAPIError(f"Unknown error: [{r.status_code}] {r.text}")

    def delete_bookmark(self, url: str) -> int:
        params = {"url": url}
        endpoint = self._build_url_with_params("rest/1/my/bookmark", params)
        r = self._request(endpoint, method="DELETE", headers=self._get_headers())
        if r.status_code in (200, 204):
            return r.status_code
        elif r.status_code == 404:
            return r.status_code
        elif r.status_code == 403:
            text = f"Permission denied: {r.text}"
            raise HatenaBookmarkAPIError(text)
        raise HatenaBookmarkAPIError(f"Unknown error: [{r.status_code}] {r.text}")

    def get_entry(self, url: str) -> Union[Entry | NotFoundEntry]:
        params = {"url": url}
        endpoint = self._build_url_with_params("rest/1/entry", params)
        r = self._request(endpoint, headers=self._get_headers())
        json_data = json.loads(r.text)
        if json_data.get("message"):
            return NotFoundEntry(**json_data)
        return Entry(**json_data)

    def get_tags(self) -> Tags:
        endpoint = self._build_url("rest/1/my/tags")
        r = self._request(endpoint, headers=self._get_headers())
        json_data = json.loads(r.text)
        return Tags(**json_data)

    def get_user_info(self) -> UserInfo:
        endpoint = self._build_url("rest/1/my")
        r = self._request(endpoint, headers=self._get_headers())
        json_data = json.loads(r.text)
        print(json_data)
        return UserInfo(**json_data)

    def get_bookmark_count(self, url: str) -> int:
        endpoint = self._build_url_with_params("count/entry", {"url": url})
        r = self._request(endpoint, headers=self._get_headers())
        if r.status_code == 200:
            return int(r.text)
        raise HatenaBookmarkAPIError(
            f"Failed to get bookmark count: [{r.status_code}] {r.text}"
        )

    def get_bookmark_counts(self, urls: List[str]) -> Dict[str, int]:
        if len(urls) > 50:
            raise ValueError("Maximum number of URLs is 50")

        params = [("url", url) for url in urls]
        endpoint = self._build_url("count/entries")
        r = self._request(endpoint, params=params, headers=self._get_headers())

        if r.status_code == 200:
            return json.loads(r.text)
        raise HatenaBookmarkAPIError(
            f"Failed to get bookmark counts: [{r.status_code}] {r.text}"
        )
