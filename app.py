from flask import jsonify, Response

from flask_restful import reqparse, abort, Api, Headers
from camera_api import camera_app
from camera_api.views import Cameras, AddCamera, CameraList, AddListenPort,PortList
from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell,Manager

import os

api = Api(camera_app)
#api = swagger.docs(Api(camera_app), apiVersion='1', api_spec_url="/api/v1/spec")
api.add_resource(Cameras, '/cameras')
api.add_resource(AddCamera, '/addcameras')
api.add_resource(CameraList, '/cameralist')
api.add_resource(AddListenPort, '/addlistenport')
api.add_resource(PortList, '/portlist')
if __name__ == '__main__':
    #db.create_all()
    camera_app.run(host='0.0.0.0',port=5000, debug=True)