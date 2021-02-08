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

from pixivapi import Client, Duration, LoginError
from pixivapi.client import AUTH_URL, BASE_URL
from tests import mocked_responses as mr


@pytest.fixture
def client():
    """For use in post-auth content-related tests."""
    c = Client()
    c.access_token = "xxx"
    return c


@pytest.fixture
def unauthed_client():
    """For use in authentication-related tests."""
    return Client()


@responses.activate
def test_login_success(unauthed_client):
    responses.add(
        responses.POST,
        AUTH_URL,
        json=mr.LOGIN_SUCCESS,
        status=200,
    )

    unauthed_client.login("bad", "credentials")
    assert unauthed_client.account is not None
    assert unauthed_client.refresh_token is not None


@responses.activate
def test_login_failure(unauthed_client):
    responses.add(
        responses.POST,
        AUTH_URL,
        json=mr.LOGIN_FAILURE,
        status=401,
    )

    with pytest.raises(LoginError):
        unauthed_client.login("bad", "credentials")

    assert unauthed_client.account is None
    assert unauthed_client.refresh_token is None


@responses.activate
def test_authentication_success(unauthed_client):
    responses.add(
        responses.POST,
        AUTH_URL,
        json=mr.LOGIN_SUCCESS,
        status=200,
    )

    unauthed_client.authenticate("good token")
    assert unauthed_client.account is not None
    assert unauthed_client.access_token is not None
    assert unauthed_client.refresh_token is not None


@responses.activate
def test_authentication_failure(unauthed_client):
    responses.add(
        responses.POST,
        AUTH_URL,
        json=mr.AUTHENTICATION_FAILURE,
        status=401,
    )

    with pytest.raises(LoginError):
        unauthed_client.authenticate("bad token")

    assert unauthed_client.account is None
    assert unauthed_client.access_token is None
    assert unauthed_client.refresh_token is None


@responses.activate
def test_search_illustrations(client, snapshot):
    responses.add(
        responses.GET,
        f"{BASE_URL}/v1/search/illust",
        json=mr.SEARCH_ILLUSTRATIONS,
        status=200,
    )

    snapshot.assert_match(
        client.search_illustrations("wlop", duration=Duration.LAST_MONTH)
    )


@responses.activate
def test_fetch_illustration(client, snapshot):
    responses.add(
        responses.GET,
        f"{BASE_URL}/v1/illust/detail",
        json=mr.FETCH_ILLUSTRATION,
        status=200,
    )

    snapshot.assert_match(client.fetch_illustration(86979680))


@responses.activate
def test_fetch_illustration_comments(client, snapshot):
    responses.add(
        responses.GET,
        f"{BASE_URL}/v1/illust/comments",
        json=mr.FETCH_ILLUSTRATION_COMMENTS,
        status=200,
    )

    snapshot.assert_match(
        client.fetch_illustration_comments(86979680, include_total_comments=True)
    )


@responses.activate
def test_fetch_illustration_related(client, snapshot):
    responses.add(
        responses.GET,
        f"{BASE_URL}/v2/illust/related",
        json=mr.FETCH_ILLUSTRATION_RELATED,
        status=200,
    )

    snapshot.assert_match(client.fetch_illustration_related(86979680))


@responses.activate
def test_fetch_illustrations_following(client, snapshot):
    responses.add(
        responses.GET,
        f"{BASE_URL}/v2/illust/follow",
        json=mr.FETCH_ILLUSTRATIONS_FOLLOWING,
        status=200,
    )

    snapshot.assert_match(client.fetch_illustrations_following())


@responses.activate
def test_fetch_illustrations_recommended(client, snapshot):
    responses.add(
        responses.GET,
        f"{BASE_URL}/v1/illust/recommended",
        json=mr.FETCH_ILLUSTRATIONS_RECOMMENDED,
        status=200,
    )

    snapshot.assert_match(client.fetch_illustrations_recommended())


@responses.activate
def test_fetch_illustrations_ranking(client, snapshot):
    responses.add(
        responses.GET,
        f"{BASE_URL}/v1/illust/ranking",
        json=mr.FETCH_ILLUSTRATIONS_RANKING,
        status=200,
    )

    snapshot.assert_match(client.fetch_illustrations_ranking())


@responses.activate
def test_fetch_trending_tags(client, snapshot):
    responses.add(
        responses.GET,
        f"{BASE_URL}/v1/trending-tags/illust",
        json=mr.FETCH_TRENDING_TAGS,
        status=200,
    )

    snapshot.assert_match(client.fetch_trending_tags())


@responses.activate
def test_fetch_bookmark(client, snapshot):
    responses.add(
        responses.GET,
        f"{BASE_URL}/v2/illust/bookmark/detail",
        json=mr.FETCH_BOOKMARK,
        status=200,
    )

    snapshot.assert_match(client.fetch_bookmark(86044539))


@responses.activate
def test_fetch_user(client, snapshot):
    responses.add(
        responses.GET,
        f"{BASE_URL}/v1/user/detail",
        json=mr.FETCH_USER,
        status=200,
    )

    snapshot.assert_match(client.fetch_user(2188232))


@responses.activate
def test_fetch_user_illustrations(client, snapshot):
    responses.add(
        responses.GET,
        f"{BASE_URL}/v1/user/illusts",
        json=mr.FETCH_USER_ILLUSTRATIONS,
        status=200,
    )

    snapshot.assert_match(client.fetch_user_illustrations(2188232))


@responses.activate
def test_fetch_user_bookmarks(client, snapshot):
    responses.add(
        responses.GET,
        f"{BASE_URL}/v1/user/bookmarks/illust",
        json=mr.FETCH_USER_BOOKMARKS,
        status=200,
    )

    snapshot.assert_match(client.fetch_user_bookmarks(126852))


@responses.activate
def test_fetch_user_bookmark_tags(client, snapshot):
    responses.add(
        responses.GET,
        f"{BASE_URL}/v1/user/bookmark-tags/illust",
        json=mr.FETCH_USER_BOOKMARK_TAGS,
        status=200,
    )

    snapshot.assert_match(client.fetch_user_bookmark_tags(126852))


@responses.activate
def test_fetch_following(client, snapshot):
    responses.add(
        responses.GET,
        f"{BASE_URL}/v1/user/following",
        json=mr.FETCH_FOLLOWING,
        status=200,
    )

    snapshot.assert_match(client.fetch_following(126852))


@responses.activate
def test_fetch_followers(client, snapshot):
    responses.add(
        responses.GET,
        f"{BASE_URL}/v1/user/follower",
        json=mr.FETCH_FOLLOWERS,
        status=200,
    )

    snapshot.assert_match(client.fetch_followers())
