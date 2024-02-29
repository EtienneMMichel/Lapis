import random
import uuid
import json
import time
from module.models.module import Module
import time
import numpy as np


class Dummy(Module):
    def __init__(self, config):
        Module.__init__(self, config)
        
        
    



    def act(self, data):
        """
        input: {matchs_infos, preds,combs, winners}
        preds: [{classic_preds:[0.4, 0.6], other_preds:[]}]
        combs: [{"mask":[0,1,0,0,1], "prob":0.4, "odd":4.6, "allocation": [0,0.3,0,0,0.7], "allocation_fund": 30}]
        DO NOT USE WINNERS variable ;)

        output: self.balance
        """

        for comb in data["combs"]:
            comb_return = self.get_return(comb=comb, winners=data["winners"])
            self.balance += comb_return
        
        self.balance_records.append(self.balance)

        return self.balance
