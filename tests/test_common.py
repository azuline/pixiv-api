from datetime import datetime, timedelta, timezone

import pytest

from pixivapi.common import format_bool, parse_qs, parse_timestamp, require_auth
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


def test_parse_timestamp():
    expected = datetime(2020, 1, 1, 0, 0, tzinfo=timezone(timedelta(seconds=32400)))
    assert parse_timestamp("2020-01-01T00:00:00+09:00") == expected


def test_parse_timestamp_no_colon():
    expected = datetime(2020, 1, 1, 0, 0, tzinfo=timezone(timedelta(seconds=32400)))
    assert parse_timestamp("2020-01-01T00:00:00+0900") == expected
