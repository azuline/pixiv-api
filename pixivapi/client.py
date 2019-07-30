from json import JSONDecodeError

from requests import RequestException, Session

from pixivapi.common import HEADERS, Struct, require_auth
from pixivapi.enums import SearchTarget, Sort
from pixivapi.errors import BadApiResponse, LoginError

AUTH_URL = 'https://oauth.secure.pixiv.net/auth/token'
BASE_URL = 'https://app-api.pixiv.net'


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
        raises: RequestException
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

    def login(self, username, password):
        """
        Log in with username and password to fetch an access token
        and a refresh token.
        """
        self._make_auth_request({
            'grant_type': 'password',
            'username': username,
            'password': password,
        })

    def authenticate(self, refresh_token):
        """
        Use a refresh token to obtain a new access token.
        """
        self._make_auth_request({
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
        })

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
        filter_='for_ios',
        duration=None,
        offset=None,
    ):
        try:
            return Struct(self._request(
                method='get',
                url=f'{BASE_URL}/v1/search/illust',
                params={
                    'word': word,
                    'search_target': search_target.value,
                    'sort': sort.value,
                    'filter': filter_,
                    **({'duration': duration.value} if duration else {}),
                    **({'offset': offset} if offset else {}),
                },
            ).json())
        except (RequestException, JSONDecodeError) as e:
            raise BadApiResponse from e
