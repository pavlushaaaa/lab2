from app.resources.data_nodes import DataNode1, DataNode2, DataNode3
from app.resources.managment_node import ManagementNode


def initialize_routes(api):
    api.add_resource(DataNode1, '/data_node1')
    api.add_resource(DataNode2, '/data_node2')
    api.add_resource(DataNode3, '/data_node3')

    api.add_resource(ManagementNode, '/manage')
