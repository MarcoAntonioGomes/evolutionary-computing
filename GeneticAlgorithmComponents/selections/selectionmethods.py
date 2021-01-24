from GeneticAlgorithmComponents.subjects.subject import Subject


class SelectionMethods:
    Vector = list[Subject]

    def __init__(self, population: Vector):
        self.population = population

    def select(self, ) -> list:
        pass
