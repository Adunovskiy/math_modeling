import matplotlib.pyplot as plt 
import numpy as np
def parabola(a = 4, b = 3, c = 1, title = 'Parabola'):
    x = np.arange(-10, 10, 0.1)
    y = a * x ** 2 + b * x + c
    plt.plot(x, y, label = 'My parabola')
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')
    plt.title(title)
    plt.legend()
    plt.show()
parabola()

def hyperbola(k = 1, title = 'Hyperbola'):
    x = np.arange(-10, 10, 0.5)
    y = k / x
    plt.plot(x, y, label = 'My hyperbola')
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')
    plt.title(title)
    plt.legend()
    plt.show()
hyperbola()

