import math
from random import random, seed

from GeneticAlgorithmComponents.mutations.mutation import Mutation


class SwapMutation(Mutation):

    def apply(self, ):
        seed(1)
        n = len(self.child)
        x = math.floor(1 + (n * random()))
        y = math.floor(1 + (n * random()))
        value_in_x = self.child[x]
        value_in_y = self.child[y]
        self.child[x] = value_in_y
        self.child[y] = value_in_x
        return self.child
