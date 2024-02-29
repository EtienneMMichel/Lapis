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
        combs: [{"mask":[0,1,0,0,1], "prob":0.4, "odd":4.6}]
        DO NOT USE WINNERS variable ;)

        output: {matchs_infos, preds,combs, winners}
        combs += "allocation": 0.3
        """

        allocations = [random.random() for _ in range(len(data["combs"]))]
        allocations = [elm/sum(allocations) for elm in allocations]
        
        return self.allocation_into_combs(data, allocations)


