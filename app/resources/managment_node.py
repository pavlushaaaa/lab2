from flask_restful import Resource, reqparse
from app.resources.data_nodes import queue_first_node, queue_third_node, queue_second_node

class ManagementNode(Resource):
    @staticmethod
    def get():
        return {"data_node1":
                    {
                        "congestion": len(queue_first_node),
                        "link": "/data_node1"
                    },
                "data_node2": {
                        "congestion": len(queue_second_node),
                        "link": "/data_node2"
                    },
                "data_node3": {
                    "congestion": len(queue_third_node),
                    "link": "/data_node3"
                }
        }

    @staticmethod
    def delete():
        parser = reqparse.RequestParser()
        parser.add_argument('node_id', required=True)
        data = parser.parse_args()
        node_id = int(data["node_id"])
        if node_id == 1:
            try:
                queue_first_node.popleft()
                return {"msg": "ok"}
            except:
                return {"msg": "queue is empty"}

        if node_id == 2:
            try:
                queue_second_node.popleft()
                return {"msg": "ok"}
            except:
                return {"msg": "queue is empty"}

        if node_id == 3:
            try:
                queue_third_node.popleft()
                return {"msg": "ok"}
            except:
                return {"msg": "queue is empty"}




