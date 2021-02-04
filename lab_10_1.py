import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)

def diff_func(r, x):
    
    y, z = r
    
    dydx = y ** 2 * z
    
    dzdy = z / x - y * z ** 2
    
    return dydx, dzdy


y0 = 1
z0 = -3
r0 = z0, y0

sol = odeint(diff_func, r0, x)

plt.plot(x, sol[:,1], 'b')