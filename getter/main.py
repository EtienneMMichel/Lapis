import redis
import json
import yaml
import sys
import module
from datetime import datetime

PUB_KEY = "forecaster"

GLOBAL_CONFIG_FETCH_INSTANCE = "getter"

def stream(instance, r):
    p = r.pubsub()
    while True:
        out_data = instance.get_data()
                    
        if not out_data is None:
            data_to_send = out_data
            data_to_send = {"type":"act", "data":out_data}
            data_to_send = json.dumps(data_to_send).encode('utf-8')
            r.publish(PUB_KEY,data_to_send)
    


if __name__ == "__main__":
    global_config = yaml.safe_load(open(sys.argv[1], "r"))
    module_config = global_config[GLOBAL_CONFIG_FETCH_INSTANCE]
    instance_name = module_config["name"]
    r = redis.Redis('localhost', 6379, charset="utf-8", decode_responses=True)
    print("SETUP INSTANCE")
    instance = eval(f"module.models.{instance_name}(module_config)")
    print("STREAM")


    stream(instance, r)