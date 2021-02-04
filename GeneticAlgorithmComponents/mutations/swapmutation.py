from random import SystemRandom

from GeneticAlgorithmComponents.mutations.mutation import Mutation


class SwapMutation(Mutation):

    random = SystemRandom()

    def apply(self, ):
        n = len(self.child)
        x = self.random.randint(0, (n - 1))
        y = self.random.randint(0, (n - 1))
        self.child[x], self.child[y] = self.child[y], self.child[x]  # Swap values in position x e y
        return self.child
