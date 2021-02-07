"""
These tests are limited in usefulness. Since we don't want these
tests to bash Pixiv's live API, they use mocked responses that were
fetched from Pixiv's API in the past.

Thus these tests live under the incorrect assumption that Pixiv's API
never changes or evolves. When the API changes, then these tests will
no longer be correct.

In the future, some tests can be added that actually run against Pixiv's
API. We can skip them on normal runs and use environment variables for
credentials.
"""

import pytest
import responses

from pixivapi import Client, LoginError
from pixivapi.client import AUTH_URL
from tests import mocked_responses as mr


@pytest.fixture
def client():
    return Client()


@responses.activate
def test_login_success(client):
    responses.add(
        responses.POST,
        AUTH_URL,
        json=mr.LOGIN_SUCCESS,
        status=200,
    )

    client.login("bad", "credentials")
    assert client.account is not None
    assert client.refresh_token is not None


@responses.activate
def test_login_failure(client):
    responses.add(
        responses.POST,
        AUTH_URL,
        json=mr.LOGIN_FAILURE,
        status=401,
    )

    with pytest.raises(LoginError):
        client.login("bad", "credentials")

    assert client.account is None
    assert client.refresh_token is None


@responses.activate
def test_authentication_success(client):
    responses.add(
        responses.POST,
        AUTH_URL,
        json=mr.LOGIN_SUCCESS,
        status=200,
    )

    client.authenticate("good token")
    assert client.account is not None
    assert client.access_token is not None
    assert client.refresh_token is not None


@responses.activate
def test_authentication_failure(client):
    responses.add(
        responses.POST,
        AUTH_URL,
        json=mr.AUTHENTICATION_FAILURE,
        status=401,
    )

    with pytest.raises(LoginError):
        client.authenticate("bad token")

    assert client.account is None
    assert client.access_token is None
    assert client.refresh_token is None
