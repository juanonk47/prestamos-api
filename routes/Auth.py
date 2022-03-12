from crypt import methods
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)