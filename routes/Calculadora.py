from crypt import methods
from flask import Blueprint
from models.Calculadora import Calculadora, calculadora_schema
calculadora = Blueprint('calculadora',__name__)

@calculadora.route('/calculadora', methods=['GET'])
# @jwt_required()
def getCalculadora():
    """Nos regresara los datos de la calculadora para el landin page donde se muestra la calculadora para iniciar la solicitud
    ---
    definitions:
      Calculadora:
        type: object
        properties:
          id:
            type: integer
          max:
            type: integer
          min:
            type: integer
          num:
            type: integer
    responses:
      200:
        description: Datos de la calculadora de prestamo
        schema:
          $ref: '#/definitions/Calculadora'
    """
    calculadora = Calculadora.query.all().pop()
    return calculadora_schema.jsonify(calculadora)