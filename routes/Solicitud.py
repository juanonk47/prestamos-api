from crypt import methods
from flask import Blueprint, request
from sqlalchemy import true
from models.Solicitud import solicitud_schema, solicituds_schema, Solicitud
from utils.db import db

solicitud = Blueprint('solicitud',__name__)

@solicitud.route('/solicitud', methods=['POST'])
def create_new_solicitud():
    """Crear nueva solicitud
    ---
    parameters:
        - in: body
          name: solicitud
          description: La solicitud a crear.
          schema:
            $ref: '#/definitions/Solicitud'
    definitions:
      Solicitud:
        type: object
        properties:
          id:
            type: integer
          valor:
            type: integer
          fecha:
            type: string
          status:
            type: boolean
          id_usuario:
            type: string
            description: Relacion del usuario
    responses:
      200:
        description: Solicitud creada
        schema:
          $ref: '#/definitions/Solicitud'
    """
    valor = request.json.get('valor',None)
    fecha = request.json.get('fecha',None)
    id_usuario = request.json.get('id_usuario',None)
    new_solicitud = Solicitud(valor,fecha,False,id_usuario)
    db.session.add(new_solicitud)
    db.session.commit()
    return solicitud_schema.jsonify(new_solicitud)

    
@solicitud.route('/solicitud/pay/<id_solicitud>',methods=['PUT'])
def pay(id_solicitud):
    """Endpoint para pagar la solicitud
    ---
    parameters:
        - in: path
          name: id_solicitud
          schema:
            type: integer
          required: true

    responses:
      200:
        description: Te muestra la solicitud pagada
        schema:
          $ref: '#/definitions/Solicitud'
      400:
        description: Muestra error por que la solicitud esta pagada
    """
    solicitud = Solicitud.query.get(id_solicitud)
    if solicitud.status:
          return {"msg": "Esta solicitud ya esta pagada"}, 400
    solicitud.status = True
    db.session.commit()
    return solicitud_schema.jsonify(solicitud)