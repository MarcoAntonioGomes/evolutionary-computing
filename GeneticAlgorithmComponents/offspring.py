from copy import deepcopy


class Offspring:

    def __init__(self, m):
      self.m = deepcopy(m)

    def __init__(self, children_1: list, children_2: list):
        self.children_1 = children_1
        self.children_2 = children_2


