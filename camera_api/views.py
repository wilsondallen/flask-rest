from flask_restful import reqparse, abort, Api, Resource
from camera_api import db
from camera_api.model import *
import json
from camera_api import camera_app
from flask import Response


def abort_if_camera_doesnt_exist(name):
    camera_query = db.session.query(MonitorCamera).filter_by(name=name).first()
    if camera_query is None:
        abort(404, message="{} doesn't exist".format(camera_query))



parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
#   show a single todo item and lets you delete them
class Cameras(Resource):
    def get(self):
        args = parser1.parse_args()
        print(args)
        name = args['name']
        abort_if_camera_doesnt_exist(name)
        camera_query = db.session.query(MonitorCamera).filter_by(name=name).first()
        camera_json = {}
        camera_json['name'] = camera_query.name
        camera_json['url'] = camera_query.url
        return camera_json

    def delete(self):
        args = parser1.parse_args()
        print(args)
        name = args['name']
        abort_if_camera_doesnt_exist(name)
        camera_query = db.session.query(MonitorCamera).filter_by(name=name).first()
        try:
            db.session.delete(camera_query)
            db.session.commit()
            return "删除成功", 200
        except Exception as e:
            return e, 400





parser1 = reqparse.RequestParser()
parser1.add_argument('name', type=str)
parser1.add_argument('url', type=str)
class AddCamera(Resource):
    def post(self):
        args = parser1.parse_args()
        print(args)
        name = args['name']
        url = args['url']
        camera_query = db.session.query(MonitorCamera).filter_by(name=name).first()
        if camera_query is not None:
            return "添加失败，当前摄像头已存在", 400
        try:
            camera = MonitorCamera(name,url)
            db.session.add(camera)
            db.session.commit()
            return "add successful", 201
        except Exception as e:
            return e, 400




class CameraList(Resource):
    def get(self):
        camera_list= []
        camera_query = MonitorCamera.query.all()
        print(camera_query)
        if camera_query is None:
            return "当前摄像头为空", 200
        else:
            for camera in camera_query:
                camera_json = {}
                camera_json['name'] = camera.name
                camera_json['url'] = camera.url
                camera_list.append(camera_json)
            return camera_list, 200


parser = reqparse.RequestParser()
parser.add_argument('url', type=str)
class AddListenPort(Resource):
    def post(self):
        args = parser.parse_args()
        url = args['url']
        listen_port_query = db.session.query(ListenPort).filter_by(url=url).first()
        if listen_port_query is not None:
            return "注册失败，当前接口已存在", 400
        try:
            listen_port = ListenPort(url)
            db.session.add(listen_port)
            db.session.commit()
            return "regest successful", 200
        except Exception as e:
            return e, 400

class PortList(Resource):
    def get(self):
        response = Response('首页', status=200, mimetype='text/html; charset=utf-8')
        return response

