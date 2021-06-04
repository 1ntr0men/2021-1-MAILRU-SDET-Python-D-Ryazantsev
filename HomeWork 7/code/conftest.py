import os
import time

import pytest
import requests
from requests.exceptions import ConnectionError

import settings
from http_client.client import Client
from mockk import flask_mock

repo_root = os.path.abspath(os.path.join(__file__, os.pardir))  # code


def start_mock():
    flask_mock.run_mock()

    started = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError('Mock did not started in 5s!')


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        start_mock()

    with open('/tmp/logger.log', "w"):
        pass


def stop_mock():
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')


def pytest_unconfigure(config):
    if not hasattr(config, 'workerinput'):
        stop_mock()


@pytest.fixture(scope="function")
def client():
    client = Client()
    yield client
    client.close()
