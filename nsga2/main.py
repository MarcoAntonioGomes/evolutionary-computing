import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pymoo.algorithms.so_genetic_algorithm import GA
from pymoo.algorithms.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.factory import get_sampling
from pymoo.interface import sample
from nsga2 import WTE
from nsga2 import WTE2
from nsga2 import WTE3

if __name__ == '__main__':
    # "one": running for first year investment
    # "two": running for 30 years
    # "three": running best ton
    # "four": running mono objective
    # "five": exploring values for x configuration
    # "six": exploring values for x ton

    # todo - revisar best ton (three, six)
    
    run = "six"

    if run == "one":
        # first analysis considering best configuration (and considering first year)
        problem = WTE(first=True)
        algorithm = NSGA2(pop_size=100)
        res = minimize(problem,
                       algorithm,
                       ('n_gen', 500),
                       seed=1,
                       verbose=True)
        fig, ax = plt.subplots()
        data = np.transpose(-res.F)
        ax.scatter(data[0], data[1])
        ax.set_title("Comportamento no primeiro ano de operação da planta WtE")
        ax.set_ylabel('Receita - Despesa (USD)')
        ax.set_xlabel('Geração em MWh/ano')
        plt.show()

    elif run == "two":
        # second analysis considering best configuration (for all years)
        problem = WTE(first=False)
        algorithm = NSGA2(pop_size=100)
        res = minimize(problem,
                       algorithm,
                       ('n_gen', 500),
                       seed=1,
                       verbose=True)
        power = problem.calculate_rsu_plant_power(res.X, 0.3)
        investment = problem.investment(power)
        fig, ax = plt.subplots()
        data = np.transpose(-res.F)
        ax.scatter(data[0], data[1])
        ax.set_title("Operação da planta WtE para 30 anos")
        ax.set_xlabel('Geração em MWh/ano')
        ax.set_ylabel('Valor Presente Líquido (USD)')
        plt.show()
        fig2, ax2 = plt.subplots()
        ax2.scatter(power, investment)
        ax2.set_title("Investimento para a planta WtE")
        ax2.set_xlabel('Potência (kW)')
        ax2.set_ylabel('Investimento (USD)')
        plt.show()

    elif run == "three":
        problem = WTE2()
        algorithm = NSGA2(pop_size=100)

        res = minimize(problem,
                       algorithm,
                       ('n_gen', 500),
                       seed=1,
                       verbose=True)
        fig, ax = plt.subplots()
        data = np.transpose(-res.F)
        ax.scatter(data[0], data[1])
        ax.set_title("Operação da planta WtE para 30 anos")
        ax.set_xlabel('Geração em MWh/ano')
        ax.set_ylabel('Valor Presente Líquido (USD)')
        plt.show()

    elif run == "four":
        problem = WTE3()
        algorithm = GA(pop_size=100, eliminate_duplicates=True)
        res = minimize(problem,
                       algorithm,
                       ('n_gen', 500),
                       seed=1,
                       verbose=False)

        print("Best solution found: \nX = %s\nF = %s" % (res.X, -res.F))

    elif run == "five":
        problem = WTE(first=True)
        sampling = get_sampling('real_random')
        vcl = np.array([712, 2729, 1921, 2490, 8193, 8633])
        x = sample(sampling, 100, 6, xl=problem.xl, xu=problem.xu)
        out = problem.evaluate(x)
        data = list(np.transpose(out[0]))
        total_x = np.sum(x, axis=1)
        total_vcl = np.sum(np.multiply(x, vcl), axis=1) / total_x
        data.append(total_x)
        data.append(total_vcl)
        df = pd.DataFrame(np.transpose(data))
        gen_sorted = df.sort_values(by=0)
        gen_sorted[0] = -gen_sorted[0]
        gen_sorted.plot(0, 2, 'scatter', title="Operação da planta WtE no ano", xlabel='Geração em MWh/ano',
                        ylabel='Total em ton/dia')
        gen_sorted.plot(0, 3, 'scatter', title="Operação da planta WtE no ano", xlabel='Geração em MWh/ano',
                        ylabel='Total em Valor Calorífico')
        plt.show()

    elif run == "six":
        problem = WTE2()
        sampling = get_sampling('real_random')
        x = sample(sampling, 100, 1, xl=problem.xl, xu=problem.xu)
        out = problem.evaluate(x)
        data = list(np.transpose(out[0]))
        total_x = np.sum(x, axis=1)
        data.append(total_x)
        df = pd.DataFrame(np.transpose(data))
        gen_sorted = df.sort_values(by=0)
        gen_sorted[0] = -gen_sorted[0]
        gen_sorted[1] = -gen_sorted[1]
        gen_sorted.plot(0, 2, 'scatter', title="Operação da planta WtE", xlabel='Geração em MWh/ano',
                        ylabel='Total em ton/dia')
        gen_sorted.plot(0, 1, 'scatter', title="Operação da planta WtE", xlabel='Geração em MWh/ano',
                        ylabel='Valor Presente Líquido (USD)')
        plt.show()
