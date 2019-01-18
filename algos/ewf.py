import numpy as np

from .exp3 import Exp3

class EWF(Exp3):
    def update_policy(self, u):
        self.T += 1
        self._update_w(u)