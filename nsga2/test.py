from pymoo.algorithms.nsga2 import NSGA2
from pymoo.factory import get_problem
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter
import autograd.numpy as anp
import numpy as np


if __name__ == '__main__':

    a = anp.array([[ 8,  9, 10, 11],
       [ 4,  5,  6,  7],
       [ 0,  1,  2,  3]])

    print( np.sum(a, axis=1) )


