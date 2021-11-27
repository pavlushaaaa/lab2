from flask_restful import Resource, reqparse
from collections import deque

queue_first_node = deque()
queue_second_node = deque()
queue_third_node = deque()


class DataNode1(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('msg', required=True)
        data = parser.parse_args()
        queue_first_node.append(data["msg"])
        return {"msg": "ok"}



class DataNode2(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('msg', required=True)
        data = parser.parse_args()
        queue_second_node.append(data["msg"])
        return {"msg": "ok"}



class DataNode3(Resource):
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('msg', required=True)
        data = parser.parse_args()
        queue_third_node.append(data["msg"])
        return {"msg": "ok"}
