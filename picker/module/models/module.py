import random
import uuid
import json
import time
import numpy as np


class Module():
    def __init__(self, config):
        pass

    def compute_prob(self, comb, preds):
        chosed_matchs_index = np.where(comb==1)[0]
        flatten_preds = np.array([pred["classic_preds"] for pred in preds]).flatten()
        return np.prod(flatten_preds[chosed_matchs_index])
    
    def compute_odd(self, comb, matchs_infos):
        chosed_matchs_index = np.where(comb==1)[0]
        flatten_odds = np.array([match_info["Odds"] for match_info in matchs_infos]).flatten()
        return np.prod(flatten_odds[chosed_matchs_index])