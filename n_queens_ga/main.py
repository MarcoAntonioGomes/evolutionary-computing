import random
from copy import deepcopy
from random import sample

import numpy as np

from GeneticAlgorithmComponents.crossovers.cutandcrossfillcrossover import CutAndCrossfillCrossover
from GeneticAlgorithmComponents.mutations.swapmutation import SwapMutation
from GeneticAlgorithmComponents.selections.tournament import Tournament
from n_queens_ga.nqueensga import NQueensGa

if __name__ == '__main__':

    population_size = 100
    maximum_number_of_generations = 10000
    crossover_probability = 0.99
    mutation_probability = 0.8
    mutation = SwapMutation()
    crossover = CutAndCrossfillCrossover()
    selection = Tournament(10)

    n_queen_ga = NQueensGa(population_size,
                           maximum_number_of_generations,
                           crossover_probability,
                           mutation_probability,
                           mutation,
                           crossover,
                           selection)

    n_queen_ga.init_population()
    n_queen_ga.run_ga()
    n_queen_ga.print_results()