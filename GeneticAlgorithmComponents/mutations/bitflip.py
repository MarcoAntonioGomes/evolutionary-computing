from GeneticAlgorithmComponents.mutations.mutation import Mutation


class BipFlip(Mutation):

    def apply(self, ):

        for i in range(len(self.child)):
            if self.child[i] == '1':
                self.child[i] = '0'
            else:
                self.child[i] = '1'

        return self.child
