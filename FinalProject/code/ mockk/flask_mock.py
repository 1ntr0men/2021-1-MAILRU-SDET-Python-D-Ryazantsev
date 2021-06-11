import json
import os
import random
import threading

from flask import Flask, jsonify, request

import settings
from mysql.sql_client import MysqlClient

app = Flask(__name__)

mysql_client = MysqlClient(user="test_qa", password="qa_test", db_name="test")
mysql_client.connect()
mysql = mysql_client


vk_ids = {}

print(mysql.check_availability("intromen"))


@app.route('/vk_id/<username>', methods=["GET"])
def get_user(username):
    if username in vk_ids:
        return jsonify({"vk_id": vk_ids[username]}), 200
    else:
        return jsonify({}), 404


if __name__ == '__main__':
    host = settings.MOCK_HOST
    port = settings.MOCK_PORT

    app.run(host, port)

    mysql_client.connection.close()
