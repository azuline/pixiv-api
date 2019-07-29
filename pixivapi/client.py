from json import JSONDecodeError

import requests
from requests import RequestError

from pixies.common import CLIENT_ID, CLIENT_SECRET, HEADERS
from pixies.errors import LoginError

AUTH_URL = 'https://oauth.secure.pixiv.net/auth/token'


class Client:

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
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'get_secure_url': 1,
        })

    def authenticate(self, refresh_token):
        """
        Use a refresh token to obtain a new access token.
        """
        self._make_auth_request({
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'get_secure_url': 1,
        })

    def _make_auth_request(self, data):
        try:
            response = requests.post(
                AUTH_URL,
                headers={
                    **HEADERS,
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                data=data,
            ).json()

            self.user = response['response']['user']
            self.access_token = response['response']['access_token']
            self.refresh_token = response['response']['refresh_token']
        except (RequestError, JSONDecodeError, KeyError) as e:
            raise LoginError from e
