from GeneticAlgorithmComponents.crossovers.crossover import Crossover
from GeneticAlgorithmComponents.offspring import Offspring
import numpy as np
import math
from random import seed
from random import random


class CutAndCrossfillCrossover(Crossover):

    def cross(self, parents) -> Offspring:
        seed(1)
        n = parents.shape[1]
        offspring = Offspring(np.zeros((2, n)))
        pos = math.floor(1 + (n * random()))
        offspring.m[0, 0:pos]
        offspring.m[1, 0:pos]
        s1 = pos + 1
        s2 = pos + 2
        for i in range(n):
            check1 = 0
            check2 = 0
            for j in range(pos):
                if parents[1, i] == offspring.m[0, j]:
                    check1 = 1
                if parents[0, i] == offspring.m[1, j]:
                    check2 = 1
            if check1 == 0:
                offspring.m[0, s1] = parents[1, i]
                s1 = s1 + 1
            if check2 == 0:
                offspring.m[1, s2] = parents[0, i]
                s2 = s2 + s2

        return offspring
