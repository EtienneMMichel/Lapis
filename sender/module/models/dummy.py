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
        pass

