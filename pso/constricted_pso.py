import numpy as np
from random import SystemRandom

'''

Constricted PSO
developed by Marco Antônio Gomes

'''


def f1(x):
    return 0


def f2(x):
    return 0


class ConstrictedPso:
    random = SystemRandom()

    def __init__(self, w, c1, c2, x, max_epochs, swarm, swarm_size, target, target_error):
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.x = x
        self.max_epochs = max_epochs
        self.swarm = swarm
        self.swarm_size = swarm_size
        self.gbest_value = float('inf')
        self.gbest_position = np.random.randint(-100, 100, 2)
        self.target = target
        self.target_error = target_error

    def set_best(self):
        for particle in self.swarm:
            fitness_value = f1(particle)
            if particle.best_value > fitness_value:
                particle.best_value = fitness_value
                particle.best_part_pos = particle.position

    def set_gbest(self):
        for particle in self.swarm:
            best_fitness_candidate = f1(particle)
            if self.gbest_value > best_fitness_candidate:
                self.gbest_value = best_fitness_candidate
                self.gbest_position = particle.position

    def move_particles(self):

        for particle in self.swarm:
            new_velocity = self.x*((self.w * particle.velocity) + (self.c1 * self.random.random()) * (
                        particle.best_part_pos - particle.position) +
                                   (self.random.random() * self.c2) * (self.gbest_position - particle.position))
            particle.velocity = new_velocity
            particle.move()

    def run(self):

        epoch = 1
        while epoch < self.max_epochs:
            self.set_best()
            self.set_gbest()

            if abs(self.gbest_value - self.target) <= self.target_error:
                break

            self.move_particles()
        epoch += 1


class Particle:

    def __init__(self, ):
        self.position = np.random.randint(-100, 100, 2)
        self.velocity = np.zeros(2)
        self.best_part_pos = self.position
        self.best_value = float('inf')

    def move(self):
        self.position = self.position + self.velocity
