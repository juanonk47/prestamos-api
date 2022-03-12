from crypt import methods
from flask import Blueprint

solicitud = Blueprint('solicitud',__name__)

@solicitud.route('/solicitud', methods=['POST'])
def create_new_solicitud():
    """Crear nueva solicitud
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
    return "CREAR NUEVA SOLICITUD"
@solicitud.route('/solicitud/pay')
def pay():
    """Endpoint para pagar la solicitud
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
    return "SOLICTUD PAGADA"