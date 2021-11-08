
from flask import Flask  # import Flask
from flask_assets import Environment


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:hendra24@localhost/kuota'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:postgres@localhost/'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
from app.controllers import *
assets = Environment(app)

