import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 3000, 10)

def bactery(m, t):
    dmdt = k * m
    return dmdt

m_0 = 100
k = 1 / 1200

solve_Bi = odeint(bactery, m_0, t)

plt.plot(t, solve_Bi[:,0], label = 'Процесс размножения бактерий')
plt.plot(t, 10 * m_0 * np.ones(len(t)))