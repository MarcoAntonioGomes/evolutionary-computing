import math
import random
from copy import deepcopy
from random import sample
import time
import numpy as np

from GeneticAlgorithmComponents.crossovers.cutandcrossfillcrossover import CutAndCrossfillCrossover
from GeneticAlgorithmComponents.mutations.swapmutation import SwapMutation
from GeneticAlgorithmComponents.selections.tournament import Tournament
from MarcoAntonioGomesRainhas.nqueensga import NQueensGa
from pso.constricted_pso import Particle, ConstrictedPso

if __name__ == '__main__':

    def sphere_function(particle: Particle):
        return sum(map(lambda x: x**2, particle.position))


    def function_rastrigin(particle: Particle):

        sum = 0
        for i in range(particle.position):
            sum = sum + (particle.position[i] ** 2) - (10 * math.cos(2 * math.pi * particle.position[i]))

        return (10 * len(particle.position)) + sum

    ncal = 100000
    population_size = 100
    max_epochs = ncal / population_size
    w = 0.729
    c1 = 1.49445
    c2 = 1.49445
    x = 1
    swarm = list()
    for i in range(population_size):
        swarm.append(Particle())
    target = 0
    target_error = 10**(-8)

    constrictedPso = ConstrictedPso(w, c1, c2, x, max_epochs, swarm, population_size,
                                    target,target_error, sphere_function)

    constrictedPso.run()
