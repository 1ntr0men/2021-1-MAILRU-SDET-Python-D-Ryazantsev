import settings
from http_client.client import Client
from mockk.flask_mock import app_data
import faker

import json

url = f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}'

fake = faker.Faker()


def add_to_data(name, surname):
    if len(app_data) == 0:
        id = 1
    else:
        id = list(app_data.values())[-1]["id"] + 1
    app_data[name] = {"id": id, "surname": surname}


class TestMockByClient:
    def test_add_user(self, client):
        name = fake.first_name()

        client.add_user(name, fake.last_name())

        assert client.check_data(name)

    def test_get_user(self, client):
        name = fake.first_name()
        add_to_data(name, fake.last_name())

        resp = client.get_user(name)

        assert json.loads(resp[-1]) == client.get_data()[name]

    def test_delete_user(self, client):
        name = fake.first_name()
        add_to_data(name, fake.last_name())

        client.delete_user(name)

        assert not client.check_data(name)

    def test_put_surname(self, client):
        name = fake.first_name()
        surname = fake.last_name()
        add_to_data(name, surname)

        client.put_user(name, "OTHER_SURNAME")
        resp = client.get_user(name)

        assert "OTHER_SURNAME" == json.loads(resp[-1])["surname"]

    def test_get_non_existent_user(self, client):
        resp = client.get_user('dnsfndksfnkjsdnfjkdsjkfnsd')
        assert "404" in resp[0]

    def test_add_existent_user(self, client):
        name = fake.first_name()
        surname = fake.last_name()
        add_to_data(name, surname)

        resp = client.add_user(name, surname)

        assert "400" in resp[0]
