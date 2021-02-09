import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0.1, 5, 0.1)

def diff_func(z, x):
    omega, y = z
    
    dydx = omega
    domegadx = - y + omega ** 2 - 3 * y ** 2 / np.sqrt(x)
    
    return domegadx, dydx

y_0 = 0.1
omega_0 = 1

z_0 = omega_0, y_0

sol = odeint(diff_func, z_0, x)

plt.plot(x, sol[:,0], 'b')

plt.plot(x, sol[:,1], 'r')