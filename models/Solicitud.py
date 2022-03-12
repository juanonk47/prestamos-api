from utils.db import db
from utils.ma import ma
from sqlalchemy.orm import relationship, backref

class Solicitud(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float())
    fecha = db.Column(db.Date())
    status = db.Column(db.Boolean())
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = relationship("Usuario", backref=backref("solicituds"))


    def __init__(self, valor,fecha,status,id_usuario):
        self.valor = valor
        self.fecha = fecha
        self.status = status
        self.id_usuario = id_usuario

class SolicitudSchema(ma.Schema):
    class Meta:
        model = Solicitud
        load_instance = True
        fields = ('id','valor','fecha','status')
solicitud_schema = SolicitudSchema()
solicituds_schema = SolicitudSchema(many=True)
