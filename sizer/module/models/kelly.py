import random
import uuid
import json
import time
from module.models.module import Module
import time
import cvxpy as cp
import numpy as np

class Kelly(Module):
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

        w = cp.Variable(len(data["combs"]))

        probs = np.array([comb["prob"] for comb in data["combs"]])
        odds = [comb["odd"] for comb in data["combs"]]
        O = np.array([odds for _ in range(len(data["combs"]))])
        obj_f = cp.sum(probs@cp.log(O@w))
        obj = cp.Maximize(obj_f)
        constraints = [sum(w) == 1, w>=0]
        prob = cp.Problem(obj, constraints)

        prob.solve()
        if prob.status == "optimal":
            allocations = np.array(w.value)
        else:
            allocations = np.zeros(len(data["combs"]))
        
        
        return self.allocation_into_combs(data, allocations)


