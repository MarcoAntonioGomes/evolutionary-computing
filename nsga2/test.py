from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
import autograd.numpy as anp

if __name__ == '__main__':

    a = anp.array([1,2,3])
    b = [1, 2, 3]

    c = a * b
