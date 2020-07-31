from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
camera_app = Flask(__name__)

camera_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'camera.sqlite')
camera_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(camera_app)