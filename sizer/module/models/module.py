import random
import uuid
import json
import time


class Module():
    def __init__(self, config):
        pass

    def allocation_into_combs(self, data, allocations):
        for i_comb in range(len(data["combs"])):
            data["combs"][i_comb]["allocation"] = allocations[i_comb]
        return data