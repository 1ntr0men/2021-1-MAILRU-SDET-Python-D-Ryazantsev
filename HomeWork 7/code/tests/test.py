import settings
from http_client.client import Client

import json

url = f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}'


class TestMockByClient:
    def test_add_user(self):
        client = Client()
        resp = client.add_user("Egor", "Egorov")
        assert "201" in resp[0]
        client.close()

    def test_get_user(self):
        client = Client()
        resp = client.get_user("Ilya")
        assert "200" in resp[0]
        client.close()

    def test_delete_user(self):
        client = Client()
        client.add_user("Delete", "Deletovich")
        client.close()

        client = Client()
        resp = client.delete_user("Delete")
        assert "200" in resp[0]
        client.close()

    def test_put_surname(self):
        client = Client()
        client.add_user("Put", "DontPutovich")
        client.close()

        client = Client()
        client.put_user("Put", "Putovich")
        client.close()

        client = Client()
        resp = client.get_user("Put")
        assert "Putovich" == json.loads(resp[-1])["surname"]
        client.close()

    def test_get_non_existent_user(self):
        client = Client()
        resp = client.get_user('dnsfndksfnkjsdnfjkdsjkfnsd')
        assert "404" in resp[0]
        client.close()

    def test_add_existent_user(self):
        client = Client()
        client.add_user('Ilya1', "Kirillov1")
        client.close()

        client = Client()
        resp = client.add_user('Ilya1', "Kirillov1")
        assert "400" in resp[0]
