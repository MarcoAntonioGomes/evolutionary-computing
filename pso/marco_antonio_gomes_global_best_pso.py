import math

from pso.global_best_pso import Particle, GlobalBestPso

if __name__ == '__main__':

    def sphere_function(particle: Particle):
        return sum(map(lambda x: ((x-0)**2), particle.position)) + (-1400)


    def function_rastrigin(particle: Particle):

        sum = 0
        for i in range(len(particle.position)):
            x = (5.12 *(particle.position[i] - 0)) / 100
            sum = sum + (x ** 2) - (10 * math.cos(2 * math.pi * x))

        return ((10 * len(particle.position)) + sum) + (-400)

    ncal = 100000
    population_size = 100
    max_epochs = ncal / population_size
    w = 1
    c1 = 1.49445
    c2 = 1.49445
    x = 1
    swarm = list()
    for i in range(population_size):
        swarm.append(Particle())
    target = 0
    target_error = 10**(-2)

    global_best_pso = GlobalBestPso(w, c1, c2, x, max_epochs, swarm, population_size,
                                   target, target_error, sphere_function)

    global_best_pso.run()
