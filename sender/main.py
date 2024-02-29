import redis
import json
import yaml
import sys
import module
from datetime import datetime

SUB_KEY = "sender"
PUB_KEY = "treasurer"

GLOBAL_CONFIG_FETCH_INSTANCE = "sender"

def init_balance_to_treasurer(instance):
    balance = instance.get_balance()
    data_to_send = {"type":"update_balance", "data":balance}
    data_to_send = json.dumps(data_to_send).encode('utf-8')
    r.publish(PUB_KEY,data_to_send)


def stream(instance, r):
    p = r.pubsub()
    p.psubscribe(SUB_KEY)
    init_balance_to_treasurer(instance)
    
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
                out_data = None
                if in_data["type"] == "backtesting_ended":
                    # VIZUALIZE
                    instance.visualize()
                    print("ENDED")
                    break
                if in_data["type"] == "act": 
                    out_data = instance.act(in_data["data"])
                    # print(instance.get_balance())
                    
                    if not out_data is None:
                        data_to_send = {"type":"update_balance", "data":out_data}
                        data_to_send = json.dumps(data_to_send).encode('utf-8')
                        r.publish(PUB_KEY,data_to_send)


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