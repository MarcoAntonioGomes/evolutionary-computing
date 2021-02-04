from GeneticAlgorithmComponents.crossovers.crossover import Crossover
from GeneticAlgorithmComponents.geneticalgorithmstructure import GeneticAlgorithmStructure
from GeneticAlgorithmComponents.mutations.mutation import Mutation
from GeneticAlgorithmComponents.selections.selectionmethods import SelectionMethods
from random import SystemRandom
import math
from rastrigin_function_ga.rastrigin_subject import RastriginSubject

'''
Function Rastrigin Minimization Genetic Algorithm 
developed by Marco Antônio Gomes
GitHub: https://github.com/MarcoAntonioGomes/evolutionary-computing/tree/master

'''


def calculate_quantity_of_bits(precision: float, xmax: float, xmin: float):
    return int(round(math.log((1 + ((xmax - xmin) / precision)), 2)))


class RastriginGa(GeneticAlgorithmStructure):
    random = SystemRandom()

    def __init__(self, population_size: int, maximum_number_of_generations: int, crossover_probability: float,
                 mutation_probability: float, mutation: Mutation, crossover: Crossover, selection_1: SelectionMethods,
                 nvar: int, precision: float, xmin: float, xmax: float, selection_2: SelectionMethods, c_max):

        super().__init__(population_size, maximum_number_of_generations, crossover_probability, mutation_probability,
                         mutation, crossover, selection_1)
        self.nvar = nvar
        self.xmin = xmin
        self.xmax = xmax
        self.selection_2 = selection_2
        self.quantity_of_bits = calculate_quantity_of_bits(precision, self.xmax, self.xmin)
        self.children_1 = None
        self.children_2 = None
        self.c_max = c_max

    def init_population(self):

        count = 1
        self.population = list()
        while count <= self.population_size:
            count_nvar = 1
            binary_string = list()
            sorted_numbers = list()
            while count_nvar <= self.nvar:

                sorted_number = self.random.randint(0, (self.quantity_of_bits ** 2) - 1)
                sorted_numbers.append(sorted_number)
                if count_nvar != 1:
                    while sorted_number in sorted_numbers:
                        sorted_number = self.random.randint(0, (self.quantity_of_bits ** 2) - 1)
                    sorted_numbers.append(sorted_number)
                binary_string.append(bin(sorted_number)[2:].zfill(self.quantity_of_bits))
                count_nvar = count_nvar + 1
            self.population.append(RastriginSubject(binary_string,
                                                    self.normalize_for_maximization(
                                                        self.function_rastrigin(binary_string))))
            count = count + 1

    # Calculate Rastrigin
    def function_rastrigin(self, binary_string: list[str]):

        sum = 0
        for i in range(self.nvar):
            real_value = self.convert_binary_to_real(binary_string[i])
            sum = sum + (real_value ** 2) - (10 * math.cos(2 * math.pi * real_value))

        return (10 * self.nvar) + sum

    # Convert binary value to real
    def convert_binary_to_real(self, binary_value_in_xi):
        return self.xmin + ((self.xmax - self.xmin) * int(binary_value_in_xi, 2)) / ((self.quantity_of_bits ** 2) - 1)

    def normalize_for_maximization(self, value):
        if self.c_max < value:
            return value
        return self.c_max - value

    def run_ga(self):
        count = 1
        best_solution_is_founded = False
        while count <= self.maximum_number_of_generations:

            father = None
            mother = None

            # Select father and mother to reproduce with 50% using 2 select methods (Tournament/Roulette)
            if self.random.random() < 0.50:
                self.selection.set_population(self.population)
                mating_pool_1 = self.selection.select()
                mating_pool_1.sort(key=lambda x: x.fitness, reverse=True)
                father = mating_pool_1[0].binary_string
                mating_pool_2 = self.selection.select()
                mating_pool_2.sort(key=lambda x: x.fitness, reverse=True)
                mother = mating_pool_1[0].binary_string

            else:
                self.selection_2.set_population(self.population)
                mating_pool_1 = self.selection_2.select()
                mating_pool_1.sort(key=lambda x: x.fitness, reverse=True)
                father = mating_pool_1[0].binary_string
                mating_pool_2 = self.selection_2.select()
                mating_pool_2.sort(key=lambda x: x.fitness, reverse=True)
                mother = mating_pool_2[0].binary_string

            if self.random.random() < self.crossover_probability:
                offspring = self.crossover.cross(father, mother)
                self.children_1 = offspring.children_1
                self.children_2 = offspring.children_2
                if self.random.random() < self.mutation_probability:
                    self.mutation.set_child(self.children_1)
                    self.children_1 = self.mutation.apply()
                    self.mutation.set_child(self.children_2)
                    self.children_2 = self.mutation.apply()

                child_1_fitness = self.normalize_for_maximization(self.function_rastrigin(self.children_1))
                child_2_fitness = self.normalize_for_maximization(self.function_rastrigin(self.children_2))
                if int(child_1_fitness) == self.c_max:
                    best_solution_is_founded = True
                    self.best_solution = self.children_1
                if int(child_2_fitness) == self.c_max:
                    best_solution_is_founded = True
                    self.best_solution = self.children_2

                self.population.append(RastriginSubject(self.children_1, child_1_fitness))
                self.population.append(RastriginSubject(self.children_2, child_2_fitness))
                if best_solution_is_founded:
                    break
            self.select_survivors()

            count = count + 1

    def select_survivors(self):
        self.population.sort(key=lambda x: x.fitness)
        self.population.pop()
        self.population.pop()

    def select_the_best_subject(self):
        self.population.sort(key=lambda x: x.fitness)
        return self.population[0]
