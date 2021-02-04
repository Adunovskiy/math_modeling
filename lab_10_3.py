import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.01)

def diff_func(z, t):
    omega, y = z
    
    dydt = omega
    
    domegadt= np.sin(x) + np.cos(x)
    
    return dydt, domegadt

x = 0
y0 = 3
omega0 = 0
z0 = omega0, y0

sol = odeint(diff_func, z0, t)

plt.plot(t, sol[:,1], 'b')
