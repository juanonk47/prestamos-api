from utils.db import db
from utils.ma import ma

class Calculadora(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    min = db.Column(db.Float)
    max = db.Column(db.Float)
    num = db.Column(db.Integer)

    def __init__(self, min,max,num):
        self.min = min
        self.max = max
        self.num = num
class CalculadoraSchema(ma.Schema):
    class Meta:
        model = Calculadora
        fields = ('id','min','max','num')
calculadora_schema = CalculadoraSchema()