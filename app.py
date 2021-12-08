from flask import Flask, request, abort

from controllers.user_controller import UserController

app = Flask(__name__)


@app.route('/v1/test')
def hello_world():
    return "Hello, World!"


@app.route('/v1/user', methods=['POST'])
def add_user():
    result = UserController.add_user(request)
    return result


@app.route('/v1/users', methods=['GET'])
def get_all_user():
    result = UserController.get_all_user()
    return result


@app.route('/v1/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    result = UserController.get_user(user_id)
    return result


@app.route('/v1/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    result = UserController.update_user(request, user_id)
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
