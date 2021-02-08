"""
The common module contains common utility functions that the rest
of the library uses.
"""

import functools
from datetime import datetime
from urllib import parse

from pixivapi.errors import AuthenticationRequired

HEADERS = {
    "User-Agent": "PixivAndroidApp/5.0.115 (Android 6.0; PixivBot)",
}


def require_auth(func):
    """
    require_auth is a decorator for methods of the Client class. If
    the client has no `access_token`, this decorator will raise an
    `AuthenticationRequired` exception.
    """

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.access_token:
            raise AuthenticationRequired
        return func(self, *args, **kwargs)

    return wrapper


def format_bool(bool_):
    """
    format_bool converts a boolean into a lowercased string.
    """
    if bool_ is None:
        return bool_
    return "true" if bool_ else "false"


def parse_qs(next_url, param):
    """
    parse_qs parses the int value of a param in a URL's query string.
    """
    next_query = parse.urlsplit(next_url).query
    val = dict(parse.parse_qsl(next_query)).get(param, None)
    return int(val) if val else None


def parse_timestamp(timestamp):
    """
    parse_timestamp parses a timestamp and returns a datetime.
    """
    # python 3.6 doesn't support colons in timestamps, but Pixiv's API
    # returns timestamps with colons.
    if ":" == timestamp[-3:-2]:
        timestamp = timestamp[:-3] + timestamp[-2:]

    return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z")
