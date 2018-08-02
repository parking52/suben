import numpy as np

class Kingdom(object):

    def __init__(self, name):
        self.name = name
        self.money = 10
        self.economy = 10
        self.army = 10
        self.v1 = 1
        self.v2 = 1
        self.moral = 1
        self.devotion = 100
        self.budget = 0

    def next_stage(self):
        ## first values are updated by the rules
        # second army effects are  and are impacting other metrics
        # third decisions from the players decisions are taken into account
        self.money += self.economy
        self.economy *= 0.9
        self.moral *= 0.9

        army_losses = 0
        self.army -= army_losses
        self.army = min(self.army, 0)

        army_allocation, economy_allocation, education_allocation, religion_allocation = self.get_orders()
        self.budget = self.economy + (self.moral * 2) + self.v1**2 + self.v2**2
        self.army += self.budget * army_allocation
        self.economy += self.budget * army_allocation
        self.moral += self.budget * education_allocation
        self.devotion += self.budget * religion_allocation


    def get_orders(self):
        vector = np.array((.25,.25,.25,.25))
        assert vector.sum() == 1
        return vector[0], vector[1], vector[2], vector[3]


