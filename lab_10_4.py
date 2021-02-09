import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.01)

def diff_func(z, t):
    omega, y = z
    
    dydt = omega
    domegadx = 4 * omega + 5 * y
    
    return domegadx, dydt

y_0 = 4
omega_0 = -1
z_0 = omega_0, y_0

sol = odeint(diff_func, z_0, t)

plt.plot(t, sol[:,0], 'b')
plt.plot(t, sol[:,1], 'b')