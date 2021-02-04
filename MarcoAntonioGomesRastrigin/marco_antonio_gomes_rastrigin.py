from GeneticAlgorithmComponents.crossovers.crossoverwithonecutoffpoint import CrossoverWithOneCutoffPoint
from GeneticAlgorithmComponents.mutations.bitflip import BipFlip
from GeneticAlgorithmComponents.selections.roulette import Roulette
from GeneticAlgorithmComponents.selections.tournament import Tournament
from MarcoAntonioGomesRastrigin.rastrigin_ga import RastriginGa


def marco_antonio(nvar, ncal):
    population_size = 100
    maximum_number_of_generations = ncal / population_size
    crossover_probability = 0.80
    mutation_probability = 0.3
    mutation = BipFlip()
    crossover = CrossoverWithOneCutoffPoint()
    selection_1 = Tournament(10)
    selection_2 = Roulette(10)
    precison = (10 ** (-3))
    xmin = -5.12
    xmax = 5.12
    c_max = 0

    rastrigin_ga = RastriginGa(population_size,
                               maximum_number_of_generations,
                               crossover_probability,
                               mutation_probability,
                               mutation,
                               crossover,
                               selection_1,
                               nvar,
                               precison,
                               xmin,
                               xmax,
                               selection_2, c_max)

    rastrigin_ga.init_population()
    rastrigin_ga.run_ga()
    the_best_subject = rastrigin_ga.select_the_best_subject()
    print("X*: ", the_best_subject.binary_string)
    print("F*: ", the_best_subject.fitness - c_max)


if __name__ == '__main__':
    marco_antonio(10, 10000)
