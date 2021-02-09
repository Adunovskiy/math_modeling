import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.1)

def diff_func(o, t):
    x, y, z = o
    dxdt = 3 * x - y + z
    dydt = x + y + z
    dzdt = 4 * x - y + 4 * z
    
    return dxdt, dydt, dzdt

x_0 = -71
y_0 = 1
z_0 = -3

o_0 = x_0, y_0, z_0

sol = odeint(diff_func, o_0, t)

plt.plot(t, sol[:,0], 'b')
plt.plot(t, sol[:,1], 'r')
plt.plot(t, sol[:,2], 'g')