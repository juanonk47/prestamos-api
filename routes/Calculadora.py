from crypt import methods
from flask import Blueprint

calculadora = Blueprint('calculadora',__name__)

@calculadora.route('/calculadora', methods=['GET'])
# @jwt_required()
def getCalculadora():
    """Nos regresara los datos de la calculadora para el landin page donde se muestra la calculadora para iniciar la solicitud
    ---
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """

    return "GET CALCULADORA"