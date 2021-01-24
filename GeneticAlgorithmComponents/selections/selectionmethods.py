from GeneticAlgorithmComponents.subjects.subject import Subject


class SelectionMethods:

    Vector = list[Subject]

    def set_population(self, population: Vector):
        self.population = population

    def select(self, ) -> list:
        pass
