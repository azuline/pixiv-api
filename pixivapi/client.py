from json import JSONDecodeError

import requests
from requests import RequestError

from pixivapi.common import HEADERS
from pixivapi.errors import LoginError

AUTH_URL = 'https://oauth.secure.pixiv.net/auth/token'


class Client:
    """An interface for the Pixiv API."""

    def __init__(
        self,
        client_id='KzEZED7aC0vird8jWyHM38mXjNTY',
        client_secret='W9JZoJe00qPvJsiyCGT3CCtC6ZUtdpKpzMbNlUGP',
    ):
        self.client_id = client_id
        self.client_secret = client_secret

        self.user_id = None
        self.access_token = None
        self.refresh_token = None

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
            r = requests.post(
                url=AUTH_URL,
                headers=HEADERS,
                data={
                    'client_id': self.client_id,
                    'client_secret': self.client_secret,
                    'get_secure_url': 1,
                    **data,
                },
            ).json()
            self.user = r['response']['user']
            self.access_token = r['response']['access_token']
            self.refresh_token = r['response']['refresh_token']
        except (RequestError, JSONDecodeError, KeyError) as e:
            raise LoginError from e

    def search_illustrations(
        self,
        word,
        search_target,
        sort,
        duration,
        filter_,
        offset,
    ):
        pass
