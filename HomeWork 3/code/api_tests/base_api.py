import pytest


class BaseApi:
    authorize = True

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, api_client):
        self.api_client = api_client
        if self.authorize:
            self.api_client.post_login("intromenoff@gmail.com", "intromen")

