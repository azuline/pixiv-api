import pytest

from pixivapi.common import format_bool, parse_qs, require_auth
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
            return True  # pragma: no cover

    with pytest.raises(AuthenticationRequired):
        Test().true()


@pytest.mark.parametrize(
    "arg, result",
    [
        (True, "true"),
        (False, "false"),
        (None, None),
    ],
)
def test_format_bool(arg, result):
    assert format_bool(arg) is result


def test_parse_qs():
    next_url = "https://localhost?next=30"
    assert parse_qs(next_url, "next") == 30
