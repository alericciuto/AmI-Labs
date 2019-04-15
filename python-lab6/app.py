from flask import Flask, jsonify, request, Response
import db_interaction

app = Flask(__name__)
api_endpoint = "/api/v1"
db_interaction.import_tasks()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route(api_endpoint + '/tasks', methods=["GET"])
def get_task_list():
    tasks = db_interaction.get_all_tasks()
    list = []
    for t in tasks:
        dictionary = dict()
        dictionary["id_task"] = t[0]
        dictionary["todo"] = t[1]
        dictionary["urgent"] = t[2]
        list.append(dictionary)
    return jsonify({"tasks":list})


@app.route(api_endpoint + '/tasks', methods=['POST'])
def add_one_task():
    task = request.json
    db_interaction.add_task(task["todo"], task["urgent"])
    return jsonify(task)


@app.route(api_endpoint + '/tasks/<id_task>', methods=['GET'])
def get_one_task(id_task):
    one_task = db_interaction.get_task(id_task)
    return jsonify(one_task)


@app.route(api_endpoint + '/tasks/<int:id_task>', methods=['PUT'])
def update_task(id_task):
    body = request.json
    db_interaction.update_task(id_task, body["todo"], body["urgent"])
    task = db_interaction.get_task(id_task)
    return jsonify(task)


@app.route(api_endpoint + '/tasks/<int:id_task>', methods=['DELETE'])
def delete_task(id_task):
    task = db_interaction.get_task(id_task)
    db_interaction.remove_task(id_task)
    return jsonify(task)


if __name__ == '__main__':
    app.run()
