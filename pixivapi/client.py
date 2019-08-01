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
    """An interface for the Pixiv API."""

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

    def _request(self, method, url, params=None, headers=None, data=None):
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

    def _get_struct(self, url, params=None):
        """
        A wrapper for JSON GET requests that recursively turns the
        fetched JSON into a python object.

        :param str url: The URL to request.
        :param dict params: The request parameters.
        """
        try:
            return Struct(
                self._request(method='get', url=url, params=params).json()
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
        return self._get_struct(
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
        return self._get_struct(
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
        return self._get_struct(
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
        return self._get_struct(
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
        return self._get_struct(
            url=f'{BASE_URL}/v2/illust/follow',
            params={
                'restrict': visibility.value,
            },
        )

    @require_auth
    def fetch_illustrations_recommended(
        self,
        offset=None,
        content_type='illust',
        include_ranking_label=True,
        max_bookmark_id_for_recommend=None,
        max_bookmark_id_for_recent_illustration=None,
        include_ranking_illustrations=None,
        bookmark_illustration_ids=None,
        include_privacy_policy=None,
    ):
        """
        Fetch new recommended illustrations. A maximum of TODO are
        returned in one response.

        Note: Some parameters are undocumented due to not knowing what
        they are.

        :param int offset: The number of illustrations to offset by.
        """
        return self._get_struct(
            url=f'{BASE_URL}/v1/illust/recommended',
            params={
                'offset': offset,
                'content_type': content_type,
                'include_ranking_label': include_ranking_label,
                'max_bookmark_id_for_recommend': max_bookmark_id_for_recommend,
                'max_bookmark_id_for_recent_illustration': (
                    max_bookmark_id_for_recent_illustration
                ),
                'include_ranking_illustrations': include_ranking_illustrations,
                'bookmark_illustration_ids': (
                    ','.join(bookmark_illustration_ids)
                ),
                'include_privacy_policy': include_privacy_policy,
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
        return self._get_struct(
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
        return self._get_struct(
            url=f'{BASE_URL}/v1/trending-tags/illust',
            params={
                'filter': FILTER,
            },
        )

    def fetch_user(self, user_id):
        """
        Fetch details about a Pixiv user.

        :param int user_id: The ID of the user.
        """
        return self._get_struct(
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
        return self._get_struct(
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
        return self._get_struct(
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
        return self._get_struct(
            url=f'{BASE_URL}/v1/user/bookmark-tags/illust',
            params={
                'restrict': visibility.value,
                'offset': offset,
            },
        )
