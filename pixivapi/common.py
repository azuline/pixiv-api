import requests

from pixivapi.errors import AuthenticationRequired

HEADERS = {
    'App-OS': 'ios',
    'Accept-Language': 'en-us',
    'App-OS-Version': '12.0.1',
    'App-Version': '7.6.2',
    'User-Agent': 'PixivIOSApp/7.6.2 (iOS 12.2; iPhone8,2)',
}


def download(url, destination):
    response = requests.get(url, stream=True)
    with open(destination, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


def require_auth(func):
    def wrapper(self, *args, **kwargs):
        if not self.access_token:
            raise AuthenticationRequired
        return func(self, *args, **kwargs)

    return wrapper
