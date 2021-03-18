import autograd.numpy as anp
import numpy as np
from pymoo.problems.util import load_pareto_front_from_file
from pymoo.model.problem import Problem


class WTE(Problem):

    def __init__(self):
        super().__init__(n_var=6, n_obj=2, n_constr=0, type_var=anp.double)
        self.xl = anp.array([0, 0, 0, 0, 0, 0])
        self.xu = anp.array([500000, 500000, 500000, 500000, 500000, 500000])
        self.vcl = anp.array([2981, 11425.78, 8042.84, 10425.13, 34302.45, 36144.64])

    def investment(self, x, alpha):
        i = 15797 * (np.sum(np.multiply(x, self.vcl), axis=1) * alpha) ** 0.82
        return i

    def _evaluate(self, x, out, *args, **kwargs):
        # Fator de capacidade
        cf = 0.75

        # Taxa de conversão para potência
        alpha = 0.0002778

        # Número de horas do ano
        h_year = 8760

        f1 = np.sum(np.multiply(x, self.vcl), axis=1) * alpha * cf * h_year

        i = self.investment(x, alpha)
        price = 100.00

        f2 = ((np.sum(np.multiply(x, self.vcl), axis=1) * alpha * cf * h_year) * price) - (0.04 * i) - i

        g1 = np.sum(x, axis=1) - 500000

        out["F"] = anp.column_stack([f1, f2])
        out["G"] = anp.column_stack([g1])
        out["G"] = - out["G"]

    def _calc_pareto_front(self):
        return load_pareto_front_from_file("osy.pf")
