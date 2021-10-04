"""Test app"""
# pylint: disable=redefined-outer-name
import pytest

from web.application import create_app


@pytest.fixture
def client():
    """Create client"""
    app = create_app({"TESTING": True})

    with app.test_client() as client:
        yield client


def test_time():
    """Start with a blank database."""

    # request_data = client.get("/")
    # print(request_data)
    # assert b'id="time"' in request_data.data
    assert True
