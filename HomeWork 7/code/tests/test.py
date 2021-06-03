import settings
from http_client.client import Client
from mockk.flask_mock import app_data

import json

url = f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}'


class TestMockByClient:
    def test_add_user(self, client):
        # client = Client()
        resp = client.add_user("Egor", "Egorov")
        assert "201" in resp[0]

        # client.close()

    def test_get_user(self, client):
        app_data["Ilya"] = {"id": 100, "surname": "Kirillov"}
        # client = Client()
        resp = client.get_user("Ilya")
        assert "200" in resp[0]
        # client.close()

    def test_delete_user(self, client):
        app_data["Delete"] = {"id": 100, "surname": "Deletovich"}
        # client = Client()
        resp = client.delete_user("Delete")
        assert "200" in resp[0]
        # client.close()

    def test_put_surname(self, client):
        app_data["Put"] = {"id": 100, "surname": "DontPutovich"}

        client.put_user("Put", "Putovich")

        resp = client.get_user("Put")
        assert "Putovich" == json.loads(resp[-1])["surname"]

    def test_get_non_existent_user(self, client):
        # client = Client()
        resp = client.get_user('dnsfndksfnkjsdnfjkdsjkfnsd')
        assert "404" in resp[0]
        # client.close()

    def test_add_existent_user(self, client):
        app_data["Ilya1"] = {"id": 100, "surname": "Kirillov1"}

        # client = Client()
        resp = client.add_user('Ilya1', "Kirillov1")
        assert "400" in resp[0]
