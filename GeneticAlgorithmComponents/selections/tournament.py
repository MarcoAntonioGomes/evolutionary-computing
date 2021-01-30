from random import randint

from GeneticAlgorithmComponents.selections.selectionmethods import SelectionMethods
from operator import attrgetter

from GeneticAlgorithmComponents.subjects.subject import Subject
from random import SystemRandom


class Tournament(SelectionMethods):
    subjects = list[Subject]
    random = SystemRandom()

    def __init__(self, k):
        self.k = k

    def select(self, ) -> list:
        current_member = 1
        u = len(self.population)
        mating_pool = []
        while current_member < u:
            count = 1
            tournament_candidates: Tournament.subjects
            tournament_candidates = list()
            while count <= self.k:
                subject_pos = self.random.randint(0, u - 1)
                tournament_candidates.append(self.population[subject_pos])
                count = count + 1
            winning_candidate = max(tournament_candidates, key=attrgetter('fitness'))
            mating_pool.append(winning_candidate)

            current_member = current_member + 1
        return mating_pool
