from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS,cross_origin

##SECURITY IMPORT
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required

##ROUTES IMPORT
from routes.Usuario import usuario
from routes.Auth import auth
from routes.Calculadora import calculadora
from routes.Solicitud import solicitud

##FLASGGER IMPORT
from flasgger import Swagger
swagger_template = {
    # Other settings

    'securityDefinitions': {
        'sso_auth': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },

    # Other settings
}



app = Flask(__name__)
CORS(app, resources={r"/": {"origins":"*"}})
swagger = Swagger(app, template=swagger_template)
ma = Marshmallow(app)

##CONFIGURE BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@127.0.0.1/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)

app.config['SECRET_KEY']='super-secret'


##SEGURIDAD Configure
jwt = JWTManager(app)


##BLUEPRINT ROUTES
app.register_blueprint(auth)
app.register_blueprint(usuario)
app.register_blueprint(calculadora)
app.register_blueprint(solicitud)