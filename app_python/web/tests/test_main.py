import pytest

from app_python.web.application import create_app


@pytest.fixture
def client():
    app = create_app({'TESTING': True})

    with app.test_client() as client:
        yield client


def test_time(client):
    """Start with a blank database."""

    rv = client.get('/')
    print(rv)
    assert b'id="time"' in rv.data