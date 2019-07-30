import requests

from pixivapi.errors import AuthenticationRequired

HEADERS = {
    'App-OS': 'ios',
    'Accept-Language': 'en-us',
    'App-OS-Version': '12.0.1',
    'App-Version': '7.6.2',
    'User-Agent': 'PixivIOSApp/7.6.2 (iOS 12.2; iPhone8,2)',
}


class Struct:
    """
    A class that takes API results and turns them into python objects.
    """
    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, self._wrap(value))

    def _wrap(self, value):
        if isinstance(value, (tuple, list, set)):
            return type(value)([self._wrap(v) for v in value])
        elif isinstance(value, dict):
            return Struct(value)
        return value


def _struct_to_dict(struct):
    """
    Development function to view all properties of API results.
    """
    def _unwrap(value):
        if isinstance(value, (tuple, list, set)):
            return type(value)([_unwrap(v) for v in value])
        elif isinstance(value, Struct):
            return _struct_to_dict(value)
        return value

    return {key: _unwrap(value) for key, value in struct.__dict__.items()}


def download(url, destination):
    response = requests.get(url, stream=True)
    with open(destination, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


def require_auth(func):
    """
    This is a decorator for methods of the Client class. If the
    client has no `access_token`, this decorator will raise an
    `AuthenticationRequired` exception.
    """
    def wrapper(self, *args, **kwargs):
        if not self.access_token:
            raise AuthenticationRequired
        return func(self, *args, **kwargs)

    return wrapper
