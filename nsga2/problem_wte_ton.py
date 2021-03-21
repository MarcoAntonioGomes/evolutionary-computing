import autograd.numpy as anp
import numpy as np
from pymoo.problems.util import load_pareto_front_from_file
from pymoo.model.problem import Problem


class WTE2(Problem):

    def __init__(self):
        super().__init__(n_var=1, n_obj=2, n_constr=0, type_var=anp.double)
        self.xl = anp.array([250])
        self.xu = anp.array([1600])
        # organica/ papel/ texteis/ plastico
        self.vcl = anp.array([712, 2729, 1921, 8193])
        self.xi = anp.array([0.62, 0.11, 0.04, 0.9])

    def investment(self, p):
        i = (15797) * (p ** 0.82)
        return i

    def total_vcl_ton(self, x):
        vcl_total = np.zeros(len(x))
        for ton in range(len(x)):
            vcl = 0
            for k in range(len(self.xi)):
                vcl = vcl + x[ton] * self.xi[k] * self.vcl[k]
            vcl_total[ton] = vcl
        return vcl_total * 4.1868

    def calculate_rsu_plant_power(self, x, electric_recovery_rate):
        p = x * electric_recovery_rate * 0.01157
        return p

    def _evaluate(self, x, out, *args, **kwargs):
        # Fator de capacidade
        cf = 0.8

        # Número de horas do ano
        h_year = 8760

        electric_recovery_rate = 0.22

        vcl_total = self.total_vcl_ton(x)

        p = self.calculate_rsu_plant_power(vcl_total, electric_recovery_rate)
        f1 = -((p * cf * h_year) / 1000)  # MWh/year

        i = self.investment(p)

        price = 51.01
        years = 25
        rate = 0.065  # 0.1

        f2 = 0

        for t in range(years):
            f2 = f2 + (((-f1 * price) - (0.04 * i)) / ((1 + rate) ** (t + 1)))

        f2 = -(f2 - i)

        f3 = years * (0.04 * i) + i

        # div = np.zeros(len(x))
        # for d in range(len(x)):
        #     div[d] = vcl_total[d] / x[d]
        #
        # g1 = (div - 8373.6) / 8373.6

        out["F"] = anp.column_stack([f1, f3])  # f2
        # out["G"] = anp.column_stack([g1])
        # out["G"] = - out["G"]
