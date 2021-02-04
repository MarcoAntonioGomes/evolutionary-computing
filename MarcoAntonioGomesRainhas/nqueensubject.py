import numpy as np

from GeneticAlgorithmComponents.subjects.subject import Subject


class NQueenSubject(Subject):

    def __init__(self, queens_positions: list[int], fitness):
        self.queens_positions = queens_positions
        super().__init__(fitness)
