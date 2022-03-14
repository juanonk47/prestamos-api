from crypt import methods
from functools import reduce
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from sqlalchemy import null
from models.Usuario import Usuario,  usuario_schema, usuarios_schema
from models.Solicitud import Solicitud, solicituds_schema
from models.Calculadora import Calculadora
from utils.db import db
import hashlib
from flask_cors import CORS,cross_origin


usuario = Blueprint('usuario', __name__)

@usuario.route('/usuario', methods=['GET'])
# @jwt_required()
@cross_origin()
def getAll():
    """Nos regresara todos los usuarios existentes
    ---
    definitions:
        usuario:
         type: object
         properties:
          id:
            type: integer
          nombre:
            type: string
          correo:
            type: string
          telefono:
            type: string
          password:
            type: string
    responses:
      200:
        description: Lista de usuarios
        schema:
          $ref: '#/definitions/usuario'
        examples:
          rgb: ['red', 'green', 'blue']
    """
    usuarios = Usuario.query.all()
    return usuarios_schema.jsonify(usuarios)

@usuario.route('/usuario', methods=['POST'])
@cross_origin()
def create_user():
    """Crear nuevo usuario
    ---
    parameters:
        - in: body
          name: user
          description: EL usuario a logear.
          schema:
            $ref: '#/definitions/usuario'
    responses:
      200:
        description: Muestra el usuario creado
        schema:
          $ref: '#/definitions/usuario'
    """
    nombre = request.json.get('nombre',None)
    correo = request.json.get('correo',None)
    telefono = request.json.get('telefono',None)
    password = request.json.get('password',None)
    d = hashlib.sha256(password.encode())
    new_user = Usuario(nombre,correo,telefono,d.hexdigest())
    db.session.add(new_user)
    db.session.commit()
    return usuario_schema.jsonify(new_user)

@usuario.route('/usuario/resetpassword', methods=['PUT'])
# @jwt_required()
@cross_origin()

def reset_password_user():
    """Resetear el password del usuario
    ---
    parameters:
        - in: body
          name: solicitud
          description: La solicitud a crear.
          schema:
            $ref: '#/definitions/UserResetPasssword'
    definitions:
        UserResetPasssword:
          type: object
          properties:
            id:
              type: integer
            oldpassword:
              type: string
            newpassword:
              type: string
    responses:
      200:
        description: SE DIO UN RESET DE CONTRASE;A CORRECTO
      400:
        description: Bad credentials
      402:
        description: No se encontro al usuario
    """
    id = request.json.get('id',None)
    newpassword = request.json.get('newpassword',None)
    oldpassword = request.json.get('oldpassword',None)
    usuario = Usuario.query.get(id)
    if usuario is None:
      return {"msg": "NO se encontro el usuario"}, 402
    elif usuario.password == oldpassword:
      usuario.password = newpassword
      db.session.commit()
      return {"msg": "Contrase;a actualizada"}, 200
    else:
      return {"msg": "Bad credentials"}, 400


@usuario.route('/usuario/solicitudes/<userid>',methods=['GET'])
# @jwt_required()
@cross_origin()

def get_all_solicitud_user(userid):
    """Obtener las solicitudes de este usuario
    ---
    parameters:
        - in: path
          name: userid
          schema:
            type: integer
          required: true
    responses:
      200:
        description: Solicitudes del usuario
        schema:
          $ref: '#/definitions/Solicitud'
      400:
        description: No existe el usuario
    """
    usuario = Usuario.query.get(userid)
    if usuario is None:
          return {"msg":"No existe el usuario"}, 400
    else:
      solicitudes = Solicitud.query.filter(Solicitud.id_usuario == usuario.id)
      return solicituds_schema.jsonify(solicitudes)
    
@usuario.route('/usuario/saldo-disponible/<userid>', methods=['GET'])
# @jwt_required()
@cross_origin()

def get_saldo_user(userid):
    """Obtener el saldo disponible del usuario
    ---
    parameters:
        - in: path
          name: userid
          schema:
            type: integer
          required: true
    responses:
      200:
        description: Saldo disponible del usuario
        content:
          application/json:
            schema:
              saldoDisponible:
                type: integer
      400:
        description: No existe el usuario
    """
    usuario = Usuario.query.get(userid)
    if usuario is None:
      return {"msg":"No existe el usuario"}, 400
    else:
      calculadora = Calculadora.query.all().pop()
      solicitudes = Solicitud.query.filter(Solicitud.id_usuario == usuario.id and Solicitud.status == False)
      valorSolicitudesNoPagasdas = 0.0
      for p in solicitudes:
            valorSolicitudesNoPagasdas += p.valor
      saldoDisponible = calculadora.max - valorSolicitudesNoPagasdas           
      return {"saldoDisponible": saldoDisponible}, 200

            