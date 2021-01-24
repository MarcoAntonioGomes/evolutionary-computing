from random import sample, random

import numpy as np

from GeneticAlgorithmComponents.geneticalgorithmstructure import GeneticAlgorithmStructure
from n_queens_ga.nqueensubject import NQueenSubject


class NQueensGa(GeneticAlgorithmStructure):

    def init_population(self):
        count = 1

        while count <= self.population_size:
            candidate = sample(range(0, 8), 8)
            self.population.append(NQueenSubject(candidate, self.calculate_candidate_fitness(candidate)))
            count = count + 1

    def calculate_candidate_fitness(self, solution):
        f = 0
        n = len(solution)
        for i in range(n):
            for j in range(n):
                if abs(i - j) == abs(solution[i] - solution[j]) and i != j:
                    f = f + 1
        f = f / 2
        return f

    def run_ga(self):
        count = 1
        best_solution_is_founded = False
        while count <= self.maximum_number_of_generations or best_solution_is_founded:

            self.selection.set_population(self.population)
            mating_pool = self.selection.select()
            mating_pool.sort(key=lambda x: x.fitness)
            father_1 = mating_pool[0]
            father_2 = mating_pool[1]
            if random.random() < self.crossover_probability:
                offspring = self.crossover.cross(np.array([father_1, father_2]))
                self.child_1 = offspring.m[0, 0:7]
                self.child_2 = offspring.m[1, 0:7]
                if random.random() < self.mutation_probability:
                    self.mutation.set_child(self.child_1)
                    self.child_1 = self.mutation.apply()
                    self.mutation.set_child(self.child_2)
                    self.child_2 = self.mutation.apply()

                child_1_fitness = self.calculate_candidate_fitness(self.child_1)
                child_2_fitness = self.calculate_candidate_fitness(self.child_2)
                if child_1_fitness == 0 or child_2_fitness == 0:
                    best_solution_is_founded = True
                self.population.append(NQueenSubject(self.child_1, child_1_fitness))
                self.population.append(NQueenSubject(self.child_2, child_2_fitness))
            self.select_survivors()

            count = count + 1

    def select_survivors(self):
        self.population.sort(key=lambda x: x.fitness)
        self.population.pop()
        self.population.pop()
