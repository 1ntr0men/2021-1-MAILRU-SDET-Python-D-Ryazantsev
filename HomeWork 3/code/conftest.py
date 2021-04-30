import pytest
from api.client import ApiClient


@pytest.fixture(scope="session")
def api_client():
    url = "https://target.my.com/"
    return ApiClient(url)
