from random import sample
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from GeneticAlgorithmComponents.crossovers.crossover import Crossover
from GeneticAlgorithmComponents.geneticalgorithmstructure import GeneticAlgorithmStructure
from GeneticAlgorithmComponents.mutations.mutation import Mutation
from GeneticAlgorithmComponents.selections.selectionmethods import SelectionMethods
from n_queens_ga.nqueensubject import NQueenSubject


def calculate_max_quantity_of_xeques():
    return (8 * (8 - 1)) / 2


class NQueensGa(GeneticAlgorithmStructure):
    c_max = 29

    def __init__(self, population_size: int, maximum_number_of_generations: int, crossover_probability: float,
                 mutation_probability: float, mutation: Mutation, crossover: Crossover, selection: SelectionMethods):
        super().__init__(population_size, maximum_number_of_generations, crossover_probability, mutation_probability,
                         mutation, crossover, selection)
        self.quantity_of_xeques = calculate_max_quantity_of_xeques()
        self.average_fitness = list()
        self.convergence_generation = None
        self.best_solution = None

    def init_population(self):

        count = 1
        self.population = list()
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
        return self.c_max - f

    def run_ga(self):
        count = 1
        best_solution_is_founded = False
        while count <= self.maximum_number_of_generations:
            print("GERAÇÃO: ", count)
            self.selection.set_population(self.population)
            mating_pool = self.selection.select()
            mating_pool.sort(key=lambda x: x.fitness, reverse=True)
            father_1 = mating_pool[0].queens_positions
            father_2 = mating_pool[1].queens_positions
            if random.random() < self.crossover_probability:
                offspring = self.crossover.cross(np.array([father_1, father_2]))
                self.child_1 = offspring.m[0, 0:8]
                self.child_2 = offspring.m[1, 0:8]
                if random.random() < self.mutation_probability:
                    self.mutation.set_child(self.child_1)
                    self.child_1 = self.mutation.apply()
                    self.mutation.set_child(self.child_2)
                    self.child_2 = self.mutation.apply()

                child_1_fitness = self.calculate_candidate_fitness(self.child_1)
                child_2_fitness = self.calculate_candidate_fitness(self.child_2)
                if int(child_1_fitness) == self.c_max:
                    best_solution_is_founded = True
                    self.best_solution = NQueenSubject(self.child_1, child_1_fitness)
                    self.convergence_generation = count
                if int(child_2_fitness) == self.c_max:
                    best_solution_is_founded = True
                    self.best_solution = NQueenSubject(self.child_2, child_2_fitness)
                    self.convergence_generation = count
                self.population.append(NQueenSubject(self.child_1, child_1_fitness))
                self.population.append(NQueenSubject(self.child_2, child_2_fitness))
                self.select_survivors()
                if best_solution_is_founded:
                    break
            self.calculate_average_fitness_per_generation()
            count = count + 1



    def select_survivors(self):
        self.population.sort(key=lambda x: x.fitness, reverse=True)
        self.population.pop()
        self.population.pop()

    def print_results(self):

        print("-------------- RESULTADOS --------------")
        pop_size = len(self.population)
        for i in range(pop_size):
            board = np.zeros((8, 8), dtype=str)
            board.fill("*")
            for j in range(8):
                board[self.population[i].queens_positions[j], j] = "X"
            print("GENOTIPO -> ", self.population[i].queens_positions)
            print("FITNESS (Numero de Colisões): ", self.population[i].fitness)
            print("QUANTIDADE MÁXIMA DE XEQUES DO TABULEIRO 8X8: ", int(self.quantity_of_xeques))
            print("TABULEIRO: ")
            print(board)
            print("-------------------------------------------------------------------------")
        if self.best_solution is None:
            print("SOLUÇÃO ÓTIMA NAO ENCONTRADA!")
        else:
            print("SOLUÇÃO ÓTIMA: ", self.best_solution.queens_positions)
            board = np.zeros((8, 8), dtype=str)
            board.fill("*")
            for j in range(8):
                board[self.best_solution.queens_positions[j], j] = "X"
            print("FITNESS (Numero de Colisões): ", self.best_solution.fitness - self.c_max)
            print("QUANTIDADE MÁXIMA DE XEQUES DO TABULEIRO 8X8: ", int(self.quantity_of_xeques))
            print("GERAÇÃO DE CONVERGÊNCIA: ", self.convergence_generation)
            print("TABULEIRO: ")
            print(board)
            print("-------------------------------------------------------------------------")

    def calculate_average_fitness_per_generation(self):
        fitness_sum = sum(x.fitness for x in self.population)
        self.average_fitness.append(fitness_sum / len(self.population))

    def plot_average_graphic_per_generation(self):

        if self.convergence_generation is None:
            return
        t = [generation for generation in range(self.convergence_generation -1)]

        fig, ax = plt.subplots()
        ax.plot(t, self.average_fitness)
        # ax.set_xlim([min(t), max(t)])
        # ax.set_ylim([min(self.average_fitness), max(self.average_fitness)])
        ax.set(xlabel='Geração', ylabel='Fitness médio',
               title='Fitness médio por geração ')
        ax.grid()

        fig.savefig("test.png")
        plt.show()
