import sys
sys.path.append('../')
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell,Manager
from camera_api import db

class MonitorCamera(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  url = db.Column(db.String(150), unique=False)

  def __init__(self, name, url):
    self.name = name
    self.url = url

  def __repr__(self):
    return '<Camera %r>' % self.name


class ListenPort(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  url = db.Column(db.String(150), unique=False)

  def __init__(self, url):
    self.url = url

  def __repr__(self):
    return '<ListenPort %r>' % self.url
