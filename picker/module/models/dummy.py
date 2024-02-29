import random
import uuid
import json
import time
from module.models.module import Module
import time
import numpy as np

MAX_NB_COMBS = 10

class Dummy(Module):
    def __init__(self, config):
        Module.__init__(self, config)

    def compute_prob(self, comb, preds):
        chosed_matchs_index = np.where(comb==1)[0]
        flatten_preds = np.array([pred["classic_preds"] for pred in preds]).flatten()
        return np.prod(flatten_preds[chosed_matchs_index])
    
    def compute_odd(self, comb, matchs_infos):
        chosed_matchs_index = np.where(comb==1)[0]
        flatten_odds = np.array([match_info["Odds"] for match_info in matchs_infos]).flatten()
        return np.prod(flatten_odds[chosed_matchs_index])
        

    def act(self, data):
        """
        input: {matchs_infos, preds, winners}
        preds: [{classic_preds:[0.4, 0.6], other_preds:[]}]
        DO NOT USE WINNERS variable ;)

        output: {matchs_infos, preds,combs, winners}
        combs: [{"mask":[0,1,0,0,1], "prob":0.4, "odd":4.6}, {"mask":[0,1,0,0,1], "prob":0.4, "odd":4.6}]
        """
        nb_matchs = len(data["matchs_infos"])
        max_comb = (2**nb_matchs if 2**nb_matchs <= MAX_NB_COMBS else MAX_NB_COMBS)
        nb_combs = random.randint(1,max_comb)
        chosed_combs = []
        for _ in range(nb_combs):
            comb = np.random.choice([0, 1], size=nb_matchs, p=[0.7, 0.3])
            chosed_combs.append({
                "mask":comb.tolist(),
                "prob":self.compute_prob(comb, data["preds"]),
                "odd": self.compute_odd(comb, data["matchs_infos"])
            })
        data["combs"] = chosed_combs
        return data


