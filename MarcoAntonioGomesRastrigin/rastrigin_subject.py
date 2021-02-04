from GeneticAlgorithmComponents.subjects.subject import Subject


class RastriginSubject(Subject):

    def __init__(self, binary_string: list[int], fitness):
        self.binary_string = binary_string
        super().__init__(fitness)
