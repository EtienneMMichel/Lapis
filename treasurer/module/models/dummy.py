import random
import uuid
import json
import time
from module.models.module import Module
import time

class Dummy(Module):
    def __init__(self, config):
        Module.__init__(self, config)

    def act(self, data):
        """
        input: {matchs_infos, preds,combs, winners}
        preds: [{classic_preds:[0.4, 0.6], other_preds:[]}]
        combs: [{"mask":[0,1,0,0,1], "prob":0.4, "odd":4.6, "allocation": [0,0.3,0,0,0.7]}]
        DO NOT USE WINNERS variable ;)

        output: {matchs_infos, preds,combs, winners}
        combs += "allocation_fund": 30
        """
        if not self.balance is None:
            for comb_id in range(len(data["combs"])):
                allocation_fund = random.randint(0, 10)
                data["combs"][comb_id]["allocation_fund"] = allocation_fund
        
        return data
        

