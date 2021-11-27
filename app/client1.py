import requests as req
import json
import time

counter = 0
num_of_requests = 100
update_frequency = 5

for i in range(num_of_requests):
    time.sleep(0.5)
    if counter == 0:
        nodes_stat = req.get('http://localhost:5000/manage')
        data = json.loads(nodes_stat.content)

        min_node_congestion = min(data["data_node1"]["congestion"], data["data_node2"]["congestion"],
                       data["data_node3"]["congestion"])
        for i in data:
            if data[i]["congestion"] == min_node_congestion:
                link = data[i]["link"]

    if link:
        req.post(f"http://localhost:5000{link}", data={"msg": "test"})
        print(f"sent info to {link}, size = {min_node_congestion}")
        counter = (counter + 1) % update_frequency

