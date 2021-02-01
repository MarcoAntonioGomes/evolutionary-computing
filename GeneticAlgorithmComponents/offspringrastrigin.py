from copy import deepcopy

from GeneticAlgorithmComponents.offspring import Offspring


class OffspringRastrigin(Offspring):

    def __init__(self, children_1: list, children_2: list, m):
        super().__init__(m)
        self.children_1 = children_1
        self.children_2 = children_2
