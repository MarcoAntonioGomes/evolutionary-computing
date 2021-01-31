from GeneticAlgorithmComponents.mutations.mutation import Mutation


class BipFlip(Mutation):

    def apply(self, ):

        for i in range(len(self.child)):
            child = ''
            for k in range(len(self.child[i])):
                if self.child[i][k] == '1':
                    child = child + '0'
                else:
                    child = child + '1'
            self.child[i] = child
        return self.child
