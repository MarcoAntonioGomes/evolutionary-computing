from copy import deepcopy

import numpy as np

if __name__ == '__main__':
    a = np.array([[1, 3, 5, 2, 6, 4, 7, 8, ], [1, 3, 5, 2, 6, 4, 7, 8]])
    c = a.shape[1]
    b = np.zeros((2, c))
    b[0, 0:4] = a[0, 0:4]
    print(a.shape)
    print(b)
    print(a[1, 2])
    x = np.empty([8])
    print(x)