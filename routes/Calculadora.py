from crypt import methods
from flask import Blueprint
from models.Calculadora import Calculadora, calculadora_schema
from flask_jwt_extended import jwt_required
from flask_cors import CORS,cross_origin
calculadora = Blueprint('calculadora',__name__)

@calculadora.route('/calculadora', methods=['GET'])
# @jwt_required()
@cross_origin()
def getCalculadora():
    """Nos regresara los datos de la calculadora para el landin page donde se muestra la calculadora para iniciar la solicitud
    ---
    security:
        - sso_auth: []
    definitions:

            type: integer
    responses:
      200:
        description: Datos de la calculadora de prestamo
        schema:
          $ref: '#/definitions/Calculadora'
    """
    calculadora = Calculadora.query.all().pop()
    return calculadora_schema.jsonify(calculadora)