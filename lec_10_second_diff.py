import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0, 2, 0.01)

def diff_func(z, x):
    y, omega = z
    
    dydx = omega
    
    domega_dx = - np.sin(y) * omega + 3 * x * y + 5
    
    return dydx, domega_dx

y0 = 0.01
omega0 = 0.05
z0 = y0, omega0

sol = odeint(diff_func, z0, x)


plt.plot(x, sol[:, 1], 'b', label = 'y(x)')
plt.plot(x, sol[:, 0], 'g', label = 'omega(x)')

plt.legend()
plt.show()


