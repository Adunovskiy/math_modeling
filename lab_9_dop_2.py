import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Пределы изменения переменный величины
# В данной задаче переменной величиной является время
t = np.arange(6, 18, 0.1)

# Запись дифф. уравнения в виде функции
def victoria(s, t):
    a = np.pi / 12 * (t - 12)
    dsdt = k * np.sqrt(s / np.pi) * E * s * np.cos(a)
    return dsdt

# Определение начальных условий
E = 1367
s_0 = 1600
k = 400 * 10 ** (-8)



# Решение дифференциального уравнения командой odeint
solve_Bi = odeint(victoria, s_0, t)

# Построение решения в виде графика функции
plt.plot(t, solve_Bi[:,0], label = 'Увеличение площади листа Виктории-Реги')