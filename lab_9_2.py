import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 8, 0.1)

def capital(n, t):
    dndt = - k * n * t
    return dndt

n_0 = 1000
k = 0.08

solve_Bi = odeint(capital, n_0, t)

plt.plot(t, solve_Bi[:,0], label = 'Инвестиции за 8 лет')





