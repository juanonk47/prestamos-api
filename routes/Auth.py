
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt
import hashlib
from flask_cors import CORS,cross_origin
import jwt

from models.Usuario import Usuario, usuarios_schema


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
@cross_origin()

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
    d = hashlib.sha256(password.encode())
    usuarios = Usuario.query.all()
    usuario = list(filter(lambda user: user.correo == correo and user.password == d.hexdigest(), usuarios))
    if len(usuario) >= 1:
          access_token = create_access_token(identity=usuario[0].correo)
          return jsonify({
            "Bearer": f'Bearer {access_token}',
            "id_usuario": f'{usuario[0].id}'
          })

    else:
          return {"msg": "Bad credentials"}, 401
          

    
