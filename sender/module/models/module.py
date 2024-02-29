import random
import uuid
import json
import time
import numpy as np
import matplotlib.pyplot as plt
DEFAULT_BALANCE = 10000

class Module():
    def __init__(self, config):
        self.balance = (config["balance"] if "balance" in list(config.keys()) else DEFAULT_BALANCE)
        self.balance_records = [self.balance]

    def get_return(self, comb, winners):
        allocation = comb["allocation"]
        allocation_fund = comb["allocation_fund"]
        mask = comb["mask"]
        odd = comb["odd"]
        comb_cost = allocation*allocation_fund
        if comb_cost > self.balance:
            comb_cost = self.balance
        if np.array(np.multiply(mask, winners) - mask).all():
            # WIN
            return comb_cost*odd - comb_cost
        
        return - comb_cost

    def visualize(self):
        plt.plot(self.balance_records)
        plt.show()

    def get_balance(self):
        return self.balance
        