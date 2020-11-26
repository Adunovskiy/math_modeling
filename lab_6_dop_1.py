import matplotlib.pyplot as plt 
import numpy as np
from numpy import sin, pi

def Lissazhu(a = 1, B = 1, A = 1, b = 2):
    p = pi / 2
    t = np.arange(0, 40, 0.01)
    x = A * sin(a * t * p)
    y = B * sin(b * t)
    plt.plot(x, y)
    plt.axis('equal')
    
Lissazhu()