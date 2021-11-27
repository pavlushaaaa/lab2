import time
import requests as req
import json

seconds_to_read = 60

for i in range(120):
    time.sleep(1)
    nodes_stat = req.get('http://localhost:5000/manage')
    data = json.loads(nodes_stat.content)
    max_node_congestion = max(data["data_node1"]["congestion"], data["data_node2"]["congestion"],
                              data["data_node3"]["congestion"])

    for i in data:
        if data[i]["congestion"] == max_node_congestion:
            link = data[i]["link"]
            if link == "/data_node1":
                node_id = 1
            if link == "/data_node2":
                node_id = 2
            if link == "/data_node3":
                node_id = 3

    req.delete("http://localhost:5000/manage", data={"node_id": node_id})

