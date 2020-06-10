import random
from Plant import Plant
class Tree(Plant):
    def __init__(self, growth_rate = None):
        super().__init__()
        self.day_actions.append(self.grow)
        self.size = 0

        if not growth_rate:
            growth_rate = random.randint(1,4)

        self.growth_rate = growth_rate
    
    def grow(self):
        self.size += self.growth_rate


        