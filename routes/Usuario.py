from crypt import methods
from flask import Blueprint
from flask_jwt_extended import jwt_required

usuario = Blueprint('usuario', __name__)

@usuario.route('/usuario', methods=['GET'])
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

@usuario.route('/usuario', methods=['POST'])
def create_user():
    """Crear nuevo usuario
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
    return "USUARIO CREADO"

@usuario.route('/usuario/resetpassword', methods=['POST'])
def reset_password_user():
    """Resetear el password del usuario
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
    return "RESET PASSWORD USER"

@usuario.route('/usuario/solicitudes/<userid>')
def get_all_solicitud_user(userid):
    """Obtener todas las solicitudes realizadas por el usuario
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
    return f'tu user #{userid}'
@usuario.route('/usuario/saldo-disponible/<userid>')
def get_saldo_user(userid):
    """Obtener el saldo disponible del usuario
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
    return f"El saldo disponible #{userid}"