import random
from copy import deepcopy
from random import sample
import time
import numpy as np

from GeneticAlgorithmComponents.crossovers.cutandcrossfillcrossover import CutAndCrossfillCrossover
from GeneticAlgorithmComponents.mutations.swapmutation import SwapMutation
from GeneticAlgorithmComponents.selections.tournament import Tournament
from MarcoAntonioGomesRainhas.nqueensga import NQueensGa

if __name__ == '__main__':
    ncal = 100000
    population_size = 100
    max_epochs = ncal / population_size
    w = 0.729
    c1 = 1.49445
    c2 = 1.49445
    x = 1




