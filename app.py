from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

##SECURITY IMPORT
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import JWTManager

##ROUTES IMPORT
from routes.Usuario import usuario
from routes.Auth import auth

##FLASGGER IMPORT
from flasgger import Swagger


app = Flask(__name__)
swagger = Swagger(app)


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