import numpy as np
from random import SystemRandom

'''

Constricted PSO
developed by Marco Antônio Gomes

'''


class Particle:

    def __init__(self, ):
        self.position = np.random.randint(-100, 100, 10)
        self.velocity = np.zeros(10)
        self.best_part_pos = self.position
        self.best_value = float('inf')

    def move(self):
        self.position = self.position + self.velocity


class ConstrictedPso:
    random = SystemRandom()

    def __init__(self, w, c1, c2, x, max_epochs, swarm, swarm_size, target, target_error, fitness_function):
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.x = x
        self.max_epochs = max_epochs
        self.swarm = swarm
        self.swarm_size = swarm_size
        self.gbest_value = float('inf')
        self.gbest_position = np.random.randint(-100, 100, 10)
        self.target = target
        self.target_error = target_error
        self.fitness_function = fitness_function

    def set_best(self):
        for particle in self.swarm:
            fitness_value = self.fitness_function(particle)
            if particle.best_value > fitness_value:
                particle.best_value = fitness_value
                particle.best_part_pos = particle.position

    def set_gbest(self):
        for particle in self.swarm:
            best_fitness_candidate = self.fitness_function(particle)
            if self.gbest_value > best_fitness_candidate:
                self.gbest_value = best_fitness_candidate
                self.gbest_position = particle.position

    def move_particles(self):

        for particle in self.swarm:
            new_velocity = self.x * ((self.w * particle.velocity) + (self.c1 * self.random.random()) * (
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
        print("A solução ótima é: ", self.gbest_position, " Época: ", epoch)
        print("Gbest: ", self.gbest_value)