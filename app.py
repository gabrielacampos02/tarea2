from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.principal import principal
from routes.messages import mensajes
from utils.db import db

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

app.register_blueprint(principal)
app.register_blueprint(mensajes)
