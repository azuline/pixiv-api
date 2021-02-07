import pytest

from pixivapi.common import require_auth
from pixivapi.errors import AuthenticationRequired


def test_require_auth_success():
    class Test:
        access_token = 1

        @require_auth
        def true(self):
            return True

    assert Test().true() is True


def test_require_auth_failure():
    class Test:
        access_token = False

        @require_auth
        def true(self):
            return True

    with pytest.raises(AuthenticationRequired):
        Test().true()
