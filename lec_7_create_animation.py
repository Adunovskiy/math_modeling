import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw = 2)

xdata, ydata = [], []

ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-2, 2)

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    anim_object.set_data(xdata, ydata)
    return anim_object,

ani = FuncAnimation(fig,
                    update,
                    frames = np.arange(0, 2 * np.pi, 0.1),
                    interval = 50
                    )
ani.save('lec_7_animation.gif')