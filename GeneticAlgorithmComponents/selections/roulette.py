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
            i = 0
            while subjects_probabilities[i] < r:
                i = i + 1
            mating_pool.append(self.population[i])
            current_member = current_member + 1
        return mating_pool

    def calculate_subjects_probabilities(self):
        fitness_total = sum(self.population, key=attrgetter('fitness'))
        subjects_probabilities = list()
        for i in range(len(self.population)):
            subjects_probabilities.append(self.population[i].fitness / fitness_total)
        return subjects_probabilities
