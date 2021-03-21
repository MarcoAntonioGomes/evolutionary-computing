import autograd.numpy as anp
import numpy as np
from pymoo.problems.util import load_pareto_front_from_file
from pymoo.model.problem import Problem


class WTE(Problem):

    def __init__(self, first=False):
        super().__init__(n_var=6, n_obj=2, n_constr=3, type_var=anp.double)
        self.xl = anp.array([100, 100, 100, 100, 100, 100])
        self.xu = anp.array([800, 800, 800, 800, 800, 800])
        # self.xl = anp.array([640, 80, 0, 0, 160, 0])
        # self.xu = anp.array([1600, 800, 400, 400, 800, 400])
        self.vcl = anp.array([712, 2729, 1921, 2490, 8193, 8633])
        self.first = first

    def investment(self, p):
        i = (15797) * (p ** 0.82)
        return i

    def calculate_rsu_plant_power(self, x, electric_recovery_rate):
        p = np.sum(np.multiply(x, (self.vcl * 4.1868)), axis=1) * electric_recovery_rate * 0.01157
        return p

    def _evaluate(self, x, out, *args, **kwargs):
        # Fator de capacidade
        cf = 0.80

        # Número de horas do ano
        h_year = 8760

        electric_recovery_rate = 0.22

        p = self.calculate_rsu_plant_power(x, electric_recovery_rate)
        f1 = -((p * cf * h_year) / 1000)  # MWh/year

        i = self.investment(p)

        price = 51.01
        years = 25
        rate = 0.065  # 0.1

        # calculo de receita/despesa para o primeiro ano
        if self.first:
            f2 = -((-f1 * price) - (0.04 * i) - i)
        else:
            # calculo de NPV para vida util da planta
            f2 = 0
            for t in range(years):
                f2 = f2 + (((-f1 * price) - (0.04 * i)) / ((1 + rate) ** (t + 1)))

            f2 = -(f2 - i)

        g1 = (- np.sum(x, axis=1) + 800) / 800
        g2 = (np.sum(x, axis=1) - 500) / 500
        g3 = ((np.sum(np.multiply(x, (self.vcl * 4.1868)), axis=1) / np.sum(x, axis=1)) - 8373.6) / 8373.6

        out["F"] = anp.column_stack([f1, f2])
        out["G"] = anp.column_stack([g1, g2, g3])
        out["G"] = - out["G"]
