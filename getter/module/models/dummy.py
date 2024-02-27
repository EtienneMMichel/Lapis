import random
import uuid
import json
import time
from module.models.module import Module
import time
import pandas as pd

class Dummy(Module):
    def __init__(self, config):
        Module.__init__(self, config)
        self.data = pd.read_csv(config["data_path"])
        self.data_length = config["data_length"]
        self.index = 0

    def get_data(self):
        matchs_infos_raw = self.data.iloc[self.index:self.index+self.data_length,:]
        self.index += self.data_length
        winners = matchs_infos_raw.pop('Winner').to_list()
        matchs_infos_raw = matchs_infos_raw.to_dict('records')
        matchs_infos = [{"Odds": [m["Odd1"], m["Odd2"]], "externals_data":m} for m in matchs_infos_raw]
        
        return [matchs_infos, winners]

