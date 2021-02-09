import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0.1, 3, 0.1)

def diff_func(z, t):
    
    omega, y = z
    
    dydt = omega
    
    domegadt = np.sqrt(1 - omega ** 2)
    
    return domegadt, dydt

y_0 = 1
omega_0 = 0.1

z_0 = omega_0, y_0

sol = odeint(diff_func, z_0, t)

plt.plot(t, sol[:,0], 'b')
plt.plot(t, sol[:,1], 'r')