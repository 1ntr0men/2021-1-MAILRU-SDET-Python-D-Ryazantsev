import json

from flask import Flask, jsonify, request

import settings

app = Flask(__name__)

SURNAME_DATA = {}
app_data = {"Ilya": {"id": 1, "surname": "Kirillov"}}
user_id_seq = 2


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


if __name__ == '__main__':
    host = settings.MOCK_HOST
    port = settings.MOCK_PORT

    app.run(host, port)
