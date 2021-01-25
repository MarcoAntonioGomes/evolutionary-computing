import math
from random import random, seed

from GeneticAlgorithmComponents.mutations.mutation import Mutation
import random


class SwapMutation(Mutation):

    def apply(self, ):
        print("------ EXECUTANDO A MUTAÇÃO: TROCA DE CROMOSSOMOS  -------")
        n = len(self.child)
        x = random.randint(0, (n - 1))
        y = random.randint(0, (n - 1))
        value_in_x = self.child[x]
        value_in_y = self.child[y]
        self.child[x] = value_in_y
        self.child[y] = value_in_x
        return self.child
