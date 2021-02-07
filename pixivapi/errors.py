"""
The errors package defines the errors used in this library's API.
"""


class PixivError(Exception):
    pass


class LoginError(PixivError):
    pass


class AuthenticationRequired(PixivError):
    pass


class BadApiResponse(PixivError):
    pass
