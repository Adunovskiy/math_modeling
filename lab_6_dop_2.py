import matplotlib.pyplot as plt 
import numpy as np
from numpy import sin, cos

def ellips(e = 1, p = 1):
    fi = np.arange(0, 1, 0.01)
    r = p / (1 + e * cos(fi))
    x = x = r * sin(fi)
    y = r * cos(fi)
    plt.plot(x, y)
    plt.axis('equal')
ellips()