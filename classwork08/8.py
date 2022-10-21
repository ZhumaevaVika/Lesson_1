import matplotlib
from matplotlib import pyplot as plt
import numpy as np

def func8(f, min_x, max_x, N, min_y, max_y):
    x = np.linspace(min_x, max_x, N)
    y = f(x)
    plt.yscale('log')
    plt.grid(True)
    plt.plot(x, y, color = 'red')
    plt.ylim((min_y, max_y))

    plt.savefig('function.jpeg')
    plt.show()

f = lambda x: x**2
min_x = 0
max_x = 10
N = 100
min_y = 0
max_y = 50
func8(f, min_x, max_x, N, min_y, max_y)