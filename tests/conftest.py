import pytest
from swagip import app


@pytest.fixture(scope='module')
def client():
    client = app.test_client()
    return client
