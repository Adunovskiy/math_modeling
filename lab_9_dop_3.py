import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Пределы изменения переменный величины
# В данной задаче переменной величиной является время
teta = np.arange(0, 2 * np.pi, 0.1)

# Запись дифф. уравнения в виде функции
def energy(vq, teta):
    dwdt = L * R ** 2 / (4 * q * vq)
    return dwdt

# Определение начальных условий
L = 3.827 * 10 ** 26
q = 147000000
R = 6371
vq = 30.4


# Решение дифференциального уравнения командой odeint
solve_Bi = odeint(energy, vq, teta)

# Построение решения в виде графика функции
plt.plot(t, solve_Bi[:,0], label = 'Увеличение площади листа Виктории-Реги')