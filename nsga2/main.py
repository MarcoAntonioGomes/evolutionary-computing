import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json
from pymoo.algorithms.so_genetic_algorithm import GA
from pymoo.algorithms.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.factory import get_sampling
from pymoo.interface import sample
from nsga2 import WTE
from nsga2 import WTE2
from nsga2 import WTE3
from pymoo.operators.crossover.simulated_binary_crossover import SimulatedBinaryCrossover


def calc_npv_value(x, power):
    price = 51.01
    years = 25
    rate = 0.065  # 0.1

    i = problem.investment(power)
    f1 = ((power * 0.8 * 8760) / 1000)

    f2 = 0
    for t in range(years):
        f2 = f2 + (((f1 * price) - (0.04 * i)) / ((1 + rate) ** (t + 1)))

    f2 = f2 - i

    return f2


if __name__ == '__main__':
    # "one": running for first year investment
    # "two": running for 30 years
    # "three": running best ton less costs
    # "four": running mono objective
    # "five": exploring values for x configuration
    # "six": exploring values for x ton

    run = "two"

    if run == "one":
        # first analysis considering best configuration (and considering first year)
        problem = WTE(first=True)
        algorithm = NSGA2(pop_size=100)
        res = minimize(problem,
                       algorithm,
                       ('n_gen', 500),
                       seed=None,
                       verbose=True)
        fig, ax = plt.subplots()
        data = np.transpose(-res.F)
        ax.scatter(data[0] / 1000, data[1] / 1E6)
        ax.set_title("Comportamento no primeiro ano de operação da planta WtE")
        ax.set_ylabel('Receita - Despesa (milhões USD)')
        ax.set_xlabel('Geração em GWh/ano')
        plt.grid()
        plt.show()
        best = np.sum(res.X, axis=1)
        fig2, ax2 = plt.subplots(2, 1)
        ax2[0].set_title("Comportamento dos objetivos em relação ao total de toneladas RSU/dia")
        ax2[0].scatter(best, data[0] / 1000)
        ax2[0].grid()
        ax2[0].set_ylabel('Geração em GWh/ano')
        ax2[1].scatter(best, data[1] / 1E6)
        ax2[1].set_ylabel('Receita - Despesa (milhões USD)')
        ax2[1].set_xlabel('ton RSU/dia')
        ax2[1].grid()
        plt.show()

    elif run == "two":
        # second analysis considering best configuration (for all years)
        problem = WTE(first=False)
        algorithm = NSGA2(pop_size=100, crossover=SimulatedBinaryCrossover(eta=15, prob=0.95))
        res = minimize(problem,
                       algorithm,
                       ('n_gen', 500),
                       seed=1,
                       verbose=True)

        x_total = np.sum(res.X, axis=1)
        vcl_total = problem.calc_vcl_total(res.X, x_total)
        power = problem.calculate_rsu_plant_power(x_total, vcl_total, 0.22)
        investment = problem.investment(power)
        fig, ax = plt.subplots()
        data = np.transpose(res.F)
        print(res.X)
        ax.scatter(-data[0] / 1000, data[1] / 1E6)
        ax.set_title("Operação da planta WtE para 25 anos")
        ax.set_xlabel('Geração em GWh/ano')
        ax.set_ylabel('Custo da Planta (milhões USD)')
        ax.grid()
        plt.show()
        fig2, ax2 = plt.subplots()
        ax2.scatter(power, investment / 1E6)
        ax2.set_title("Investimento para a planta WtE")
        ax2.set_xlabel('Potência (kW)')
        ax2.set_ylabel('Investimento (milhões USD)')
        ax2.grid()
        plt.show()
        print(len(res.X))
        fig3, ax3 = plt.subplots(2, 1)
        ax3[0].set_title("Comportamento dos objetivos em relação ao total de toneladas RSU/dia")
        ax3[0].scatter(x_total, -data[0] / 1000)
        ax3[0].grid()
        ax3[0].set_ylabel('Geração em GWh/ano')
        ax3[1].scatter(x_total, data[1] / 1E6)
        ax3[1].set_ylabel('Custo da Planta (milhões USD)')
        ax3[1].set_xlabel('ton RSU/dia')
        ax3[1].grid()
        plt.show()
        npv = calc_npv_value(res.X, power)
        fig4, ax4 = plt.subplots()
        ax4.scatter(x_total, npv / 1E6)
        ax4.set_title("Valor Presente Líquido")
        ax4.set_xlabel('ton RSU/dia')
        ax4.set_ylabel('VPL (milhões USD)')
        ax4.grid()
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
        data = np.transpose(res.F)
        ax.scatter(-data[0] / 1000, data[1]/1E6)
        ax.set_title("Operação da planta WtE para 25 anos")
        ax.set_xlabel('Geração em GWh/ano')
        # ax.set_ylabel('Valor Presente Líquido (milhões) USD)')
        ax.grid()
        ax.set_ylabel('Custo da planta em 25 anos (milhões USD)')
        fig2, ax2 = plt.subplots()
        print(res.X)
        data2 = np.transpose(res.X)
        ax2.scatter(data2, -data[0] / 1000)
        ax2.set_title("Operação da planta WtE para 25 anos")
        ax2.set_xlabel('Toneladas RSU/dia')
        ax2.set_ylabel('Geração em GWh/ano')
        ax2.grid()
        plt.show()

    elif run == "four":
        problem = WTE3()
        algorithm = GA(pop_size=100, eliminate_duplicates=True)
        res = minimize(problem,
                       algorithm,
                       ('n_gen', 500),
                       seed=1,
                       verbose=True)

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
                        ylabel='Total em Valor Calorífico (kcal/kg)')
        plt.show()

    elif run == "six":
        problem = WTE2()
        sampling = get_sampling('real_random')
        x = sample(sampling, 100, 1, xl=problem.xl, xu=problem.xu)
        out = problem.evaluate(x)
        data = list(np.transpose(out))
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



