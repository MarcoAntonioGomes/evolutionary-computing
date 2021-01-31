from GeneticAlgorithmComponents.selections.selectionmethods import SelectionMethods
from random import SystemRandom
from operator import attrgetter

from GeneticAlgorithmComponents.subjects.subject import Subject


class Roulette(SelectionMethods):
    subjects = list[Subject]
    random = SystemRandom()

    def __init__(self, k):
        self.k = k

    def select(self, ) -> list:
        current_member = 1
        u = len(self.population)
        mating_pool = []
        subjects_probabilities = self.calculate_subjects_probabilities()
        while current_member < self.k:
            r = self.random.random()
            r = float("{:.2f}".format(r))
            i = 0
            while subjects_probabilities[i] < r:
                if i == len(subjects_probabilities)-1:
                    break
                i = i + 1

            mating_pool.append(self.population[i])
            current_member = current_member + 1
        return mating_pool

    def calculate_subjects_probabilities(self):
        self.population.sort(key=lambda x: x.fitness)
        fitness_total = sum(x.fitness for x in self.population)
        subjects_probabilities = list()
        previous_probability = 0.0
        for i in range(len(self.population)):
            previous_probability = previous_probability + float("{:.2f}".format(self.population[i].fitness / fitness_total))
            subjects_probabilities.append(float("{:.2f}".format(previous_probability)))
        return subjects_probabilities
