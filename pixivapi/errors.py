class PixivError(Exception):
    pass


class AuthenticationRequired(PixivError):
    pass
