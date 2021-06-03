import json
import threading

from flask import Flask, jsonify, request

import settings

app = Flask(__name__)

SURNAME_DATA = {}
app_data = {}
user_id_seq = 1


@app.route('/add_user', methods=["POST"])
def create_user():
    global user_id_seq
    user_name = json.loads(request.data)['name']
    if user_name not in app_data:
        if "surname" in json.loads(request.data):
            data = {"id": user_id_seq, "surname": json.loads(request.data)['surname']}
        else:
            data = {"id": user_id_seq, "surname": ""}
        user_id_seq += 1
        app_data[user_name] = data
        return jsonify(data), 201
    else:
        return jsonify(f'User name {user_name} already exists'), 400


@app.route('/get_user/<name>', methods=["GET"])
def get_user(name):
    if name in app_data:
        return jsonify(app_data[name]), 200
    else:
        return jsonify(f"User {name} not found"), 404


@app.route('/delete_user/<name>', methods=["DELETE"])
def delete_user(name):
    if name in app_data:
        return jsonify(f'User {app_data.pop(name)} successful deleted'), 200
    else:
        return jsonify(f'User don`t found'), 404


@app.route('/update_surname', methods=["PUT"])
def update_surname():
    user_name = json.loads(request.data)['name']
    new_surname = json.loads(request.data)['surname']
    if user_name in app_data:
        app_data[user_name]["surname"] = new_surname
        return jsonify(f'Surname changed successful'), 200
    else:
        return jsonify(f'User don`t found'), 404


@app.route('/get_data', methods=["GET"])
def get_data():
    return jsonify(app_data), 200


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'OK, exiting'), 200
