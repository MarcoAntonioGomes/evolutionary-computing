from random import randint

from GeneticAlgorithmComponents.selections.selectionmethods import SelectionMethods
from operator import attrgetter

from GeneticAlgorithmComponents.subjects.subject import Subject


class Tournament(SelectionMethods):

    subjects = list[Subject]

    def __init__(self, population, k):
        self.k = k
        self().__init__(population)

    def select(self, ) -> list:
        current_member = 1
        u = len(self.population)
        mating_pool = []
        while current_member < u:
            count = 1
            tournament_candidates: Tournament.subjects
            while count <= self.k:
                subject_pos = randint(0, u - 1)
                tournament_candidates.append(self.population[subject_pos])
                winning_candidate = max(self.population, key=attrgetter('fitness'))
                mating_pool.append(winning_candidate)
                count = count + 1
        return mating_pool
