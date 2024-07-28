from typing import Optional, Dict, List
from urllib.parse import urlencode

import pandas as pd
import feedparser
from feedparser import FeedParserDict

from .model import FeedEntry

ENTRIES_PER_PAGE = 40


class HatenaBookmarkFeedClient:
    BASE_URL = "https://b.hatena.ne.jp/search"

    def search(
        self,
        search_type: str,
        q: str,
        sort: str = "recent",
        users: Optional[int] = None,
        date_begin: Optional[str] = None,
        date_end: Optional[str] = None,
        skip: int = 0,
        limit: Optional[int] = None,
        max_pages: int = 1,
    ) -> List[FeedEntry]:
        params = self._build_params(q, sort, users, date_begin, date_end)
        data: FeedEntry = self._fetch_data(search_type, params, skip, limit, max_pages)
        self.df = pd.DataFrame(data).drop_duplicates(subset=["id", "link"])
        return self.df.to_dict(orient="records")

    def _build_params(
        self,
        q: str,
        sort: str,
        users: Optional[int],
        date_begin: Optional[str],
        date_end: Optional[str],
    ) -> Dict[str, str]:
        params = {"q": q, "mode": "rss", "sort": sort}
        if users:
            params["users"] = str(users)
        if date_begin:
            params["date_begin"] = date_begin
        if date_end:
            params["date_end"] = date_end
        return params

    def _fetch_data(
        self,
        search_type: str,
        params: Dict[str, str],
        skip: int,
        limit: Optional[int],
        max_pages: int,
    ) -> List[FeedEntry]:
        data: List[FeedEntry] = []
        for page in range(1, max_pages + 1):
            params["of"] = str((page - 1) * ENTRIES_PER_PAGE)
            url = f"{self.BASE_URL}/{search_type}?{urlencode(params)}"
            feed = feedparser.parse(url)

            print(f"Page {page}: {len(feed.entries)} entries")

            for entry in feed.entries:
                if skip > 0:
                    skip -= 1
                    continue

                data.append(self._parse_entry(entry))

                if limit and len(data) >= limit:
                    return data[:limit]

            if len(feed.entries) < ENTRIES_PER_PAGE:
                break

        return data

    def _parse_entry(self, entry: FeedParserDict) -> FeedEntry:
        return {
            "id": entry.id,
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary,
            "updated": entry.updated,
            "hatena_bookmarkcount": getattr(entry, "hatena_bookmarkcount", None),
            "hatena_bookmarkcommentlistpageurl": getattr(
                entry, "hatena_bookmarkcommentlistpageurl", None
            ),
            "hatena_imageurl": getattr(entry, "hatena_imageurl", None),
        }
