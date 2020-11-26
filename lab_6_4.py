import matplotlib.pyplot as plt 
import numpy as np
def ladder(N = 0):
    x = np.arange(0, 15, 0.001)
    y = []
    for i in range(len(x)):
        a = x[i] // 1
        y.append(a)
    plt.plot(x, y)
    plt.show()
ladder(2)