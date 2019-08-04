import functools
from urllib import parse

from pixivapi.errors import AuthenticationRequired

HEADERS = {
    'App-OS': 'ios',
    'Accept-Language': 'en-us',
    'App-OS-Version': '12.0.1',
    'App-Version': '7.6.2',
    'User-Agent': 'PixivIOSApp/7.6.2 (iOS 12.2; iPhone8,2)',
}


def require_auth(func):
    """
    This is a decorator for methods of the Client class. If the
    client has no `access_token`, this decorator will raise an
    `AuthenticationRequired` exception.
    """
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.access_token:
            raise AuthenticationRequired
        return func(self, *args, **kwargs)

    return wrapper


def format_bool(bool_):
    if bool_ is None:
        return bool_
    return 'true' if bool_ else 'false'


def parse_qs(next_url, param):
    next_query = parse.urlsplit(next_url).query
    val = dict(parse.parse_qsl(next_query)).get(param, None)
    return int(val) if val else None
