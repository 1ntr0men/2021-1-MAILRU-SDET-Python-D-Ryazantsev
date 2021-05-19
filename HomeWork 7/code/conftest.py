import os
import signal
import subprocess
import sys
import time
from copy import copy

import requests
from requests.exceptions import ConnectionError

import settings


repo_root = os.path.abspath(os.path.join(__file__, os.pardir))  # code


def start_mock(config):
    mock_path = os.path.join(repo_root, 'mockk', 'flask_mock.py')

    mock_out = open('/tmp/mock_stdout.log', 'w')
    mock_err = open('/tmp/mock_stderr.log', 'w')

    env = copy(os.environ)
    env['MOCK_HOST'] = settings.MOCK_HOST
    env['MOCK_PORT'] = settings.MOCK_PORT

    proc = subprocess.Popen([sys.executable, mock_path], stdout=mock_out, stderr=mock_err, env=env)

    config.mock_proc = proc
    config.mock_out = mock_out
    config.mock_err = mock_err

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
        start_mock(config)

    with open('/tmp/logger.log', "w"):
        pass


def stop_mock(config):
    config.mock_proc.send_signal(signal.SIGINT)
    exit_code = config.mock_proc.wait()

    config.mock_out.close()
    config.mock_err.close()

    assert exit_code == 0


def pytest_unconfigure(config):
    if not hasattr(config, 'workerinput'):
        stop_mock(config)
