import random
import uuid
import json
import time
from module.models.module import Module
import time

class Dummy(Module):
    def __init__(self, config):
        Module.__init__(self, config)

    def get_pred(self, match_info):
        probs = [random.random() for _ in range(len(match_info["Odds"]))]
        probs = [p/sum(probs) for p in probs]
        return {"classic_preds":probs, "other_preds":[]}

    def act(self, data):
        """
        input: {matchs_infos, winners}
        DO NOT USE WINNERS variable ;)

        output: {matchs_infos, preds, winners}
        preds: [{classic_preds:[0.4, 0.6], other_preds:[]}]
        """
        preds = []
        for match_info in data["matchs_infos"]:
            pred = self.get_pred(match_info)
            preds.append(pred)

        data["preds"] = preds

        return data



