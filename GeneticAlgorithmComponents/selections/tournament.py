from random import randint

from GeneticAlgorithmComponents.selections.selectionmethods import SelectionMethods
from operator import attrgetter

class Tournament(SelectionMethods):

    def __init__(self, population, k):
        self.k = k
        self().__init__(population)

    def select(self, ) -> list:
        current_member = 1
        u = len(self.population)
        mating_pool = []
        while current_member < u:
            count = 1
            tournament_candidates = []
            while count <= self.k:
                subject_pos = randint(0, u - 1)
                tournament_candidates.append(self.population[subject_pos])
                winning_candidate = max(self.population, key=attrgetter('fitness'))
                mating_pool.append(winning_candidate)
        return mating_pool
    