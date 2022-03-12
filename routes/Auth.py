
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt

from models.Usuario import Usuario, usuarios_schema


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    """Auth del usuario
    ---
    parameters:
        - in: body
          name: user
          description: EL usuario a logear.
          schema:
            $ref: '#/definitions/UserLogin'
    definitions:
        UserLogin:
         type: object
         properties:
          correo:
            type: string
          password:
            type: string
    responses:
      200:
        description: Success and token!
      401:
        description: Bad credentials!
    """
    correo = request.json.get('correo',None)
    password = request.json.get('password', None)

    usuarios = Usuario.query.all()
    usuario = list(filter(lambda user: user.correo == correo and user.password == password, usuarios))
    if len(usuario) >= 1:
          access_token = create_access_token(identity=usuario[0].correo)
          return jsonify(access_token)
    else:
          return {"msg": "Bad credentials"}, 401
          

    
