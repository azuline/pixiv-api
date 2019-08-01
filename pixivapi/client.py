from json import JSONDecodeError

from requests import RequestException, Session

from pixivapi.common import HEADERS, Struct, require_auth
from pixivapi.enums import (
    ContentType,
    RankingMode,
    SearchTarget,
    Sort,
    Visibility,
)
from pixivapi.errors import BadApiResponse, LoginError

AUTH_URL = 'https://oauth.secure.pixiv.net/auth/token'
BASE_URL = 'https://app-api.pixiv.net'
FILTER = 'for_ios'


class Client:
    """A client for the Pixiv API."""

    def __init__(
        self,
        client_id='KzEZED7aC0vird8jWyHM38mXjNTY',
        client_secret='W9JZoJe00qPvJsiyCGT3CCtC6ZUtdpKpzMbNlUGP',
    ):
        self.client_id = client_id
        self.client_secret = client_secret

        self.account = None
        self.access_token = None
        self.refresh_token = None

        self.session = Session()
        self.session.headers.update(HEADERS)

    def _request(
        self,
        method,
        url,
        params=None,
        headers=None,
        data=None,
    ):
        """
        A wrapper around ``requests.Session.request`` that adds the
        access token to the request headers if present.

        :param str method: The request method. Typically ``'get'``
            or ``'post'``.
        :param str url: The URL to request.
        :param dict params: The request parameters.
        :param dict headers: The request headers.
        :param dict data: The request data.

        :raises: requests.RequestException
        """
        # headers has a sentinel value to avoid unsafe mutable default kwarg.
        return self.session.request(
            method=method,
            url=url,
            headers={
                **(
                    {'Authorization': f'Bearer {self.access_token}'}
                    if self.access_token else {}
                ),
                **(headers or {}),
            },
            params=params,
            data=data,
        )

    def _request_struct(
        self,
        method,
        url,
        params=None,
        headers=None,
        data=None,
    ):
        """
        A wrapper for JSON requests that recursively turn the fetched JSON into
        a python object.

        :param str url: The URL to request.
        :param dict params: The request parameters.
        :param str method: The HTTP method.
        """
        try:
            return Struct(
                self._request(method=method, url=url, params=params).json()
            )
        except (RequestException, JSONDecodeError) as e:
            raise BadApiResponse from e

    def login(self, username, password):
        """
        Log in with username and password to fetch an access token
        and a refresh token.

        :param str username: Your username.
        :param str password: Your password.
        """
        self._make_auth_request(
            {
                'grant_type': 'password',
                'username': username,
                'password': password,
            }
        )

    def authenticate(self, refresh_token):
        """
        Use a refresh token to obtain a new access token.

        :param str refresh_token: The refresh token.
        """
        self._make_auth_request(
            {
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token,
            }
        )

    def _make_auth_request(self, data):
        try:
            r = self._request(
                method='post',
                url=AUTH_URL,
                data={
                    'client_id': self.client_id,
                    'client_secret': self.client_secret,
                    'get_secure_url': 1,
                    **data,
                },
            ).json()
            self.account = Struct(r['response']['user'])
            self.access_token = r['response']['access_token']
            self.refresh_token = r['response']['refresh_token']
        except (RequestException, JSONDecodeError, KeyError) as e:
            raise LoginError from e

    @require_auth
    def search_illustrations(
        self,
        word,
        search_target=SearchTarget.TAGS_PARTIAL,
        sort=Sort.DATE_DESC,
        duration=None,
        offset=None,
    ):
        """
        Search the illustrations. A maximum of TODO are returned in
        one response.

        :param str word: The search term.
        :param SearchTarget search_target: The target for the search term.
        :param Sort sort: How to sort the illustrations.
        :param Duration duration: An optional max-age for the illustrations.
        :param int offset: The number of illustrations to offset by.
        """
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v1/search/illust',
            params={
                'word': word,
                'search_target': search_target.value,
                'sort': sort.value,
                'duration': duration.value if duration else None,
                'offset': offset,
                'filter': FILTER,
            },
        )

    def fetch_illustration(self, illustration_id):
        """
        Fetch the details of a single illustration.

        :param int illustration_id: The ID of the illustration.
        """
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v1/illust/detail',
            params={
                'illust_id': illustration_id,
            }
        )

    def fetch_illustration_comments(
        self,
        illustration_id,
        offset=None,
        include_total_comments=False,
    ):
        """
        Fetch the comments of an illustration. A maximum of TODO are
        returned in one response.

        :param int illustration_id: ID of the illustration.
        :param int offset: Number of comments to offset by.
        :param bool include_total_comments: TODO figure out what this does.
        """
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v1/illust/comments',
            params={
                'illust_id': illustration_id,
                'offset': offset,
                'include_total_comments': include_total_comments,
            },
        )

    def fetch_illustration_related(self, illustration_id, offset=None):
        """
        Fetch illustrations related to a specified illustration. A
        maximum of TODO are returned in one response.

        :param int illustration_id: ID of the illustration.
        :param int offset: Illustrations to offset by.
        """
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v2/illust/related',
            params={
                'illust_id': illustration_id,
                'offset': offset,
            },
        )

    @require_auth
    def fetch_illustrations_following(
        self,
        visibility=Visibility.PUBLIC,
        offset=None,
    ):
        """
        Fetch new illustrations from followed artists. A maximum of TODO
        are returned in one response.

        :param Visibility visibility: Visibility of the followed artist;
            ``PUBLIC`` if publicly followed; ``PRIVATE`` if privately.
        :param int offset: The number of illustrations to offset by.
        """
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v2/illust/follow',
            params={
                'restrict': visibility.value,
            },
        )

    @require_auth
    def fetch_illustrations_recommended(self, offset=None):
        """
        Fetch new recommended illustrations. A maximum of TODO are
        returned in one response.

        :param int offset: The number of illustrations to offset by.
        """
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v1/illust/recommended',
            params={
                'offset': offset,
            },
        )

    def fetch_illustrations_ranking(
        self,
        mode=RankingMode.DAY,
        date=None,
        offset=None,
    ):
        """
        Fetch the ranking illustrations. A maximum of TODO are returned
        in one response.

        :param RankingMode mode: The ranking list to fetch.
        :param str date: The date of the list, in ``%Y-%m-%d`` format.
        :param int offset: The number of illustrations to offset by.
        """
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v1/illust/ranking',
            params={
                'mode': mode,
                'date': date,
                'offset': offset,
                'filter': FILTER,
            },
        )

    def fetch_trending_tags(self):
        """
        Fetch the trending tags for illustrations.
        """
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v1/trending-tags/illust',
            params={
                'filter': FILTER,
            },
        )

    @require_auth
    def fetch_bookmark(self, illustration_id):
        """
        Fetch details about a bookmarked illustration.

        :param int illustration_id: The ID of the bookmarked illustration.
        """
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v2/illust/bookmark/detail',
            params={
                'illust_id': illustration_id,
            },
        )

    @require_auth
    def add_bookmark(
        self,
        illustration_id,
        visibility=Visibility.PUBLIC,
        tags=None,
    ):
        """
        Bookmark an illustration.

        :param int illustration_id: The ID of the illustration.
        :param Visibility visibility: The visibility of the bookmark.
        :param List[str] tags: Tags to assign to the bookmark.
        """
        return self._request_struct(
            method='post',
            url=f'{BASE_URL}/v2/illust/bookmark/add',
            data={
                'illust_id': illustration_id,
                'restrict': visibility.value,
                'tags': ' '.join(tags) if tags else tags,
            },
        )

    @require_auth
    def delete_bookmark(self, illustration_id):
        """
        Delete a bookmark for an illustration.

        :param int illustration_id: The ID of the illustration.
        """
        return self._request_struct(
            method='post',
            url=f'{BASE_URL}/v1/illust/bookmark/delete',
            data={
                'illust_id': illustration_id,
            },
        )

    def fetch_user(self, user_id):
        """
        Fetch details about a Pixiv user.

        :param int user_id: The ID of the user.
        """
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v1/user/detail',
            params={
                'user_id': user_id,
                'filter': FILTER,
            },
        )

    def fetch_user_illustrations(
        self,
        user_id,
        type_=ContentType.ILLUSTRATIONS,
        offset=None,
    ):
        """
        Fetch the illustrations posted by a user.

        :param int user_id: The ID of the user.
        :param ContentType type_: The type of content to fetch.
        :param int offset: The number of illustrations/manga to offset by.
        """
        # TODO: Check to see if 'illust' includes manga. If not, try None.
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v1/user/illusts',
            params={
                'user_id': user_id,
                'type': type_.value if type_ else None,
                'offset': offset,
                'filter': FILTER,
            },
        )

    @require_auth
    def fetch_user_bookmarks(
        self,
        user_id,
        visibility=Visibility.PUBLIC,
        max_bookmark_id=None,
        tag=None,
    ):
        """
        Fetch the illustrations bookmarked by a user. A maximum of TODO
        illustrations are returned in a response.

        :param int user_id: The ID of the user.
        :param Visibility visibility: The visibility of the bookmarks.
            Applies only to requests for one's own bookmarks.
        :param int max_bookmark_id: The ID of the maximum bookmark,
            similar to ``offset`` for other endpoints.
        :param str tag: The bookmark tag to filter bookmarks by. These tags
            can be fetched from ``Client.fetch_user_bookmark_tags``.
        """
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v1/user/bookmarks/illust',
            params={
                'user_id': user_id,
                'restrict': visibility.value,
                'max_bookmark_id': max_bookmark_id,
                'tag': tag,
            },
        )

    @require_auth
    def fetch_user_bookmark_tags(
        self,
        visibility=Visibility.PUBLIC,
        offset=None,
    ):
        """
        Fetch the bookmark tags that belong to the user. A maximum of
        TODO tags are returned in a response.

        :param Visibility visibility: The visibility of the tags.
        :param int offset: The number of tags to offset by.
        """
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v1/user/bookmark-tags/illust',
            params={
                'restrict': visibility.value,
                'offset': offset,
            },
        )

    @require_auth
    def fetch_following(
        self,
        user_id,
        visibility=Visibility.PUBLIC,
        offset=None,
    ):
        """
        Fetch the users that a user is following. A maximum of TODO
        users are returned in a response.

        :param int user_id: The ID of the user.
        :param Visibility visibility: The visibility of the followed
            users. Applies only when fetching one's own followed users.
        :param int offset: The number of users to offset by.
        """
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v1/user/following',
            params={
                'user_id': user_id,
                'restrict': visibility.value,
                'offset': offset,
            },
        )

    @require_auth
    def fetch_followers(self, user_id, offset=None):
        """
        Fetch the users that are following a user. A maximum of TODO
        users are returned in a response.

        :param int user_id: The ID of the user.
        :param int offset: The number of users to offset by.
        """
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v1/user/follower',
            params={
                'user_id': user_id,
                'offset': offset,
                'filter': FILTER,
            },
        )

    @require_auth
    def fetch_my_pixiv(self, user_id, offset=None):
        """
        TODO: Figure out what this fetches.

        :param int user_id: The ID of the user.
        :param int offset: The number of TODO to offset by.
        """
        return self._request_struct(
            method='get',
            url=f'{BASE_URL}/v2/user/list',
            params={
                'user_id': user_id,
                'offset': offset,
                'filter': FILTER,
            },
        )
