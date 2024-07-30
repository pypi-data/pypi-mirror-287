from collections.abc import Iterator
from typing import Any, Callable

from ...models import BaseSnippet, Playlist
from ...schemas import (
    CreatePlaylist,
    PlaylistFilter,
    PlaylistOptionalParameters,
    PlaylistPart,
    YouTubeListResponse,
    YouTubeRequest,
    YouTubeResponse,
)
from ..resource import YouTubeResource


class PlaylistItemIterator(Iterator):
    def __init__(
        self,
        request_creator: Callable[[YouTubeRequest], dict],
        youtube_client: Any,
        response_parser: Callable[[dict], YouTubeResponse],
        request_schema: YouTubeRequest,
    ) -> None:
        super().__init__()
        self._playlists_schema: YouTubeRequest = request_schema
        self._playlists_nxt_page_tkn: str = None
        self._request_creator = request_creator
        self._youtube_client: Any = youtube_client
        self._response_parser = response_parser
        self._done: bool = False

    def __iter__(self):
        return self

    def __next__(self) -> list[Playlist]:
        if self._done:
            raise StopIteration()
        self._playlists_schema.optional_parameters.pageToken = (
            self._playlists_nxt_page_tkn
        )
        request_dict = self._request_creator(self._playlists_schema)
        find_channel_playlist_request: dict = self._youtube_client.playlistItems().list(
            **request_dict
        )
        find_channel_resp: dict = find_channel_playlist_request.execute()
        find_channel_playlist_result: YouTubeResponse = self._response_parser(
            find_channel_resp
        )
        self._playlists_nxt_page_tkn = find_channel_playlist_result.nextPageToken
        if not self._playlists_nxt_page_tkn:
            self._done = True
        return find_channel_playlist_result.items
