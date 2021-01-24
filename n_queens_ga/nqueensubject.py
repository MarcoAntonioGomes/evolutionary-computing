import numpy as np

from GeneticAlgorithmComponents.subjects.subject import Subject


class NQueenSubject(Subject):

    def __init__(self, fitness):
        self.queens_positions = np.empty([8])
        self().__init__(fitness)
