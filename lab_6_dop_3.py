import matplotlib.pyplot as plt 
import numpy as np

def func(a=2, b=1, x=1):
    x = np.arange(-5, 5, 1)
    y = []
    for i in range(len(x)):
        if x[i] < a:
            y.append(a**2)
        if x[i] >= a and x[i] <= b:
            y.append(x[i]**2)
        if x[i] > b:
            y.append(b**2)
    plt.plot(x, y)
    plt.axis('equal')
func()
            
    