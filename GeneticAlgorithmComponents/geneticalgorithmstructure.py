from GeneticAlgorithmComponents.crossovers.crossover import Crossover
from GeneticAlgorithmComponents.mutations.mutation import Mutation
from GeneticAlgorithmComponents.selections.selectionmethods import SelectionMethods
from GeneticAlgorithmComponents.subjects.subject import Subject

'''
Genetic Algorithm Structure
developed by Marco Antônio Gomes
GitHub: https://github.com/MarcoAntonioGomes/evolutionary-computing/tree/master

'''


class GeneticAlgorithmStructure:
    population = list[Subject]

    def __init__(self, population_size: int,
                 maximum_number_of_generations: int,
                 crossover_probability: float,
                 mutation_probability: float,
                 mutation: Mutation,
                 crossover: Crossover,
                 selection: SelectionMethods):
        self.population_size = population_size
        self.maximum_number_of_generations = maximum_number_of_generations
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability
        self.mutation = mutation
        self.crossover = crossover
        self.selection = selection
        self.best_solution = []

    def init_population(self):
        pass

    def calculate_candidate_fitness(self, solution):
        pass

    def run_ga(self):
        pass
