import random
import uuid
import json
import time
from module.models.module import Module
import time
import numpy as np


class MostProbableByMatch(Module):
    def __init__(self, config):
        Module.__init__(self, config)

    
        

    def act(self, data):
        """
        input: {matchs_infos, preds, winners}
        preds: [{classic_preds:[0.4, 0.6], other_preds:[]}]
        DO NOT USE WINNERS variable ;)

        output: {matchs_infos, preds,combs, winners}
        combs: [{"mask":[0,1,0,0,1], "prob":0.4, "odd":4.6}, {"mask":[0,1,0,0,1], "prob":0.4, "odd":4.6}]
        """
        nb_matchs = len(data["matchs_infos"])
        nb_combs = nb_matchs
        chosed_combs = []
        for i in range(nb_combs):
            comb = [[0,0] for _ in range(nb_matchs)]
            comb[i] = ([1,0] if data["preds"][i]["classic_preds"][0] >= data["preds"][i]["classic_preds"][1] else [0,1])
            comb = np.array(comb).flatten()
            chosed_combs.append({
                "mask":comb.tolist(),
                "prob":self.compute_prob(comb, data["preds"]),
                "odd": self.compute_odd(comb, data["matchs_infos"])
            })
        data["combs"] = chosed_combs
        return data


