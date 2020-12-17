import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, exp
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
butterfly, = plt.plot([], [],'-', color = 'r')

xdata = []
ydata = []

edge = 20
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


def update(t):
    
    x0 = 0
    y0 = 0
    xdata.append(x0 + sin(t) * (exp(cos(t)) - 2 * cos(4 * t) + sin(t / 12) ** 5))
    ydata.append(y0 + cos(t) * (exp(cos(t)) - 2 * cos(4 * t) + sin(t / 12) ** 5))
    butterfly.set_data(xdata, ydata)
    return butterfly,


    
ani = FuncAnimation(fig,
                    update,
                    frames = np.arange(0, 2 * np.pi, 0.1),
                    interval = 30
                    )
ani.save('lab_7_3_1.gif')

