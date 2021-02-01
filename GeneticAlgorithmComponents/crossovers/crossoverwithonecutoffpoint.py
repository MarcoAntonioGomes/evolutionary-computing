from GeneticAlgorithmComponents.crossovers.crossover import Crossover
from GeneticAlgorithmComponents.offspring import Offspring
from random import SystemRandom

from GeneticAlgorithmComponents.offspringrastrigin import OffspringRastrigin


class CrossoverWithOneCutoffPoint(Crossover):
    random = SystemRandom()

    def cross(self, father: list, mother: list) -> Offspring:
        n = len(father)
        children_1 = list()
        children_2 = list()
        for i in range(n):
            variable_i_father = father[i]
            variable_i_mother = mother[i]
            quantity_of_bits = len(variable_i_father)
            cutoff_point = self.random.randint(0, (quantity_of_bits - 1))

            variable_i_children_1 = None
            variable_i_children_2 = None

            variable_i_children_1 = variable_i_father[0:cutoff_point]
            variable_i_children_2 = variable_i_mother[0:cutoff_point]

            for k in range(cutoff_point, quantity_of_bits):
                if variable_i_father[k] == '1':
                    variable_i_children_1 = variable_i_children_1 + '0'
                else:
                    variable_i_children_1 = variable_i_children_1 + '1'
                if variable_i_mother[k] == '1':
                    variable_i_children_2 = variable_i_children_2 + '0'
                else:
                    variable_i_children_2 = variable_i_children_2 + '1'
            children_1.append(variable_i_children_1)
            children_2.append(variable_i_children_2)
        return OffspringRastrigin(children_1, children_2, None)
