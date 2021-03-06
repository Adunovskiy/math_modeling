import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 200

t = np.linspace(0, 5, frames)

def move_func(z, t):
    x, v_x, y, v_y = z
    dxdt = v_x
    dv_xdt = 0 
    dydt = v_y
    dv_ydt = - g
    return dxdt, dv_xdt, dydt, dv_ydt

g = 9.8
v_0 = 15
alpha = 80 * np.pi / 180
x_0 = 0
v_x0 = v_0 * np.cos(alpha)
y_0 = 0
v_y0 = v_0 * np.sin(alpha)
z_0 = x_0, v_x0, y_0, v_y0

def solve_func(i, key):
    sol = odeint(move_func, z_0, t)
    if key == 'point':
        x = sol[i,0]
        y = sol[i,2]
    else:
        x = sol[:i, 0]
        y = sol[:i, 2]
    return x, y

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color = 'r')
ball_line, = plt.plot([], [], '-', color = 'r')

def animate(i):
    ball.set_data(solve_func(i, 'point'))
    ball_line.set_data(solve_func(i, 'line'))

ani = FuncAnimation (fig,
                     animate,
                     frames = frames,
                     interval = 30
                     )
edge = 15
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

plt.show()