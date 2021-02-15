'''

Constricted PSO
developed by Marco Antônio Gomes

'''
import numpy as np

def f1(x):
    return 0


def f2(x):
    return 0

class ConstrictedPso:

    def __init__(self, w, c1, c2, x, max_epochs, swarm, swarm_size):
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.x = x
        self.max_epochs = max_epochs
        self.swarm = swarm
        self.swarm_size = swarm_size


    def set_best(self):
        for i in range(self.swarm_size):
            if (f1(self.swarm[i]) )


    def run(self):

        epoch = 1
        while epoch < self.max_epochs:




class Particle:

    def __init__(self,):
        self.position = np.random.randint(-100,100,10)
        self.velocity = np.zeros(10)
        self.best_part_pos = self.position
        self.value = float('inf')




