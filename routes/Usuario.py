from flask import Blueprint
from flask_jwt_extended import jwt_required

usuario = Blueprint('usuario', __name__)

@usuario.route('/usuario')
@jwt_required()
def getAll():
    """Nos regresara todos los usuarios existentes
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


    
    return "getall"
