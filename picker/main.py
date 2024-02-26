import redis
import json
import yaml
import sys
import module
from datetime import datetime

SUB_KEY = "picker"
PUB_KEY = "sizer"

GLOBAL_CONFIG_FETCH_INSTANCE = "picker"

def stream(instance, r):
    p = r.pubsub()
    p.psubscribe(SUB_KEY)
    while True:
        # listen to odd_request
        message = p.get_message()
        if message is not None and isinstance(message, dict) :
            # print(message["data"])
            # print(isinstance(message["data"], dict))
            try:
                in_data = json.loads(message["data"])
            except TypeError:
                in_data = None
            if isinstance(in_data, dict):
                # --------------------------------------------------------
                if in_data["type"] == "act": 
                    instance.send_request(in_data["data"])


                # elif backtesting and in_data["type"] == "backtesting_ended":
                #     print("BACKTESTING ENDED")
                #     break
                
                # --------------------------------------------------------
                


if __name__ == "__main__":
    global_config = yaml.safe_load(open(sys.argv[1], "r"))
    module_config = global_config[GLOBAL_CONFIG_FETCH_INSTANCE]
    instance_name = module_config["name"]
    r = redis.Redis('localhost', 6379, charset="utf-8", decode_responses=True)
    print("SETUP INSTANCE")
    instance = eval(f"module.models.{instance_name}(module_config)")
    print("STREAM")


    stream(instance, r)