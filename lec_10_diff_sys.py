import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определяемая величина

t = np.arange(0, 10, 0.1)

# Функция для решения дифф. уравнений

def diff_func(z, t): # z - изменяемая для всей системы
    theta, omega = z # Указание изменяемых функций, через z
    
    # Первое уравнение системы
    dtheta_dt = omega
    
    # Второе уравнение системы
    domega_dt = - b * omega - c * np.sin(omega)
    
    return dtheta_dt, domega_dt

theta0 = np.pi - 0.1
omega0 = 1

# Начальные значения
z0 = theta0, omega0

b = 0.25
c = 5.0

# Решение
sol = odeint(diff_func, z0, t)

# График
plt.plot(t, sol[:, 1], 'b', label = 'omega(t)')

plt.legend()
plt.show()
    