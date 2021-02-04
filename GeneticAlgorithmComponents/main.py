import random
from random import sample

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
    print(sample(range(0, 8), 8))
    print(random.random())
    e = [1, 3, 5, 2, 6, 4, 7, 8, ]
    f = [1, 3, 5, 2, 6, 4, 7, 8, ]
    c = a.shape[1]
    g = np.array([e, f])
    print(a)
    print(g)
    print( np.zeros((8,8)))
    print(random.randint(0, 7))
    for i in range(8):
        print(i)
    print(np.zeros((8,8)))
    print( f'{6:010b}')
    q = 10
    n = 5
    print(bin(n)[2:].zfill(q))
    print(10**2)