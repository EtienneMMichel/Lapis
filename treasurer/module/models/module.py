import random
import uuid
import json
import time

class Module():
    def __init__(self, config):
        self.balance = None

    def update_balance(self, new_balance):
        self.balance = new_balance