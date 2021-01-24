import math
from random import random, seed

from GeneticAlgorithmComponents.mutations.mutation import Mutation


class SwapMutation(Mutation):

    def apply(self, ):
        seed(1)
        n = len(self.chromosome)
        x = math.floor(1 + (n * random()))
        y = math.floor(1 + (n * random()))
        value_in_x = self.chromosome[x]
        value_in_y = self.chromosome[y]
        self.chromosome[x] = value_in_y
        self.chromosome[y] = value_in_x
        return self.chromosome
