import logging
import shutil
import os

import allure

from api.api_client import ApiClient
from mysql.sql_client import MysqlClient
from ui.fixtures import *


def pytest_configure(config):
    base_test_dir = '/tmp/tests'

    if not hasattr(config, 'workerinput'):
        if os.path.exists(base_test_dir):
            shutil.rmtree(base_test_dir)
        os.makedirs(base_test_dir)

        mysql_client = MysqlClient(user="test_qa", password="qa_test", db_name="test")
        # mysql_client.recreate_db()
        #
        mysql_client.connect()
        # mysql_client.create_test_users()
        mysql_client.clear_test_users()
        #
        mysql_client.connection.close()

    config.base_test_dir = base_test_dir


@pytest.fixture(scope='session')
def base_temp_dir():
    base_dir = '/tmp/tests'
    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    os.makedirs(base_dir)
    return base_dir


@pytest.fixture(scope='function')
def test_dir(base_temp_dir, request):
    test_dir = os.path.join(base_temp_dir, request._pyfuncitem.nodeid)
    os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope="session")
def mysql_client():
    mysql_client = MysqlClient(user="test_qa", password="qa_test", db_name="test")
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()


@pytest.fixture(scope="session")
def api_client():
    url = "http://127.0.0.1:8080/"
    return ApiClient(url)


@pytest.fixture(scope='function', autouse=True)
def logger(test_dir):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)-15s - %(levelname)-6s - %(message)s')
    log_file = os.path.join(test_dir, 'test.log')

    log_level = logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()

    with open(log_file, 'r') as f:
        allure.attach(f.read(), 'test.log', attachment_type=allure.attachment_type.TEXT)
