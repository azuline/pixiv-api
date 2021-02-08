import pytest

from pixivapi import Client


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
