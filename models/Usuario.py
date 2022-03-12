from utils.db import db
from utils.ma import ma
from sqlalchemy.orm import relationship

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    correo = db.Column(db.String(100))
    telefono = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, nombre,correo,telefono,password):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.password = password
class UsuarioSchema(ma.Schema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True
        fields = ('id','nombre','correo','telefono','password')
usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
