from .exp3p import Exp3P

class Exp3(Exp3P):
    def __init__(self, actions, η):
        super().__init__(actions, η, 0, 0)