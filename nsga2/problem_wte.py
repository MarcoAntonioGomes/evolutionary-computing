import autograd.numpy as anp
import numpy as np
from pymoo.problems.util import load_pareto_front_from_file
from pymoo.model.problem import Problem


class WTE(Problem):

    def __init__(self):
        super().__init__(n_var=6, n_obj=2, n_constr=1, type_var=anp.double)
        self.xl = anp.array([0, 0, 0, 0, 0, 0])
        self.xu = anp.array([955, 955, 955, 955, 955, 955])
        self.vcl = anp.array([712, 2729, 1921, 2490, 8193, 8633])

    def investment(self, p):
        i = (15797) * (p ** 0.82)
        return i

    def calculate_rsu_plant_power(self, x, electric_recovery_rate):
        p = np.sum(np.multiply(x, (self.vcl * 4.1868)), axis=1) * electric_recovery_rate * 0.01157
        return p

    def _evaluate(self, x, out, *args, **kwargs):
        # Fator de capacidade
        cf = 0.75

        # Número de horas do ano
        h_year = 8760

        electric_recovery_rate = 0.3

        p = self.calculate_rsu_plant_power(x, electric_recovery_rate)
        f1 = -((p * cf * h_year) / 1000)

        i = self.investment(p)

        price = 45.00
        years = 30
        rate = 0.1

        # f2 = -(((-f1 * price) * 30) - (30 * (0.04 * i)) - i)
        f2 = 0

        for t in range(years):
            f2 = f2 +(((-f1 * price) - (0.04 * i))/((1 + rate)**(t+1)))

        f2 = -(f2 - i)

        g1 = (- np.sum(x, axis=1) + 955) / 955

        out["F"] = anp.column_stack([f1, f2])
        out["G"] = anp.column_stack([g1])
        out["G"] = - out["G"]

    def _calc_pareto_front(self):
        return load_pareto_front_from_file("osy.pf")
