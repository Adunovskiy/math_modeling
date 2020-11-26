import matplotlib.pyplot as plt 
import numpy as np
from numpy import pi
from numpy import sin, cos, pi, exp
from numpy import sqrt

def spyral(b=1):
    fi = np.arange(0, 30, 0.1)
    r = exp(b * fi)
    x = r * sin(fi)
    y = r * cos(fi)
    plt.plot(x, y)
    plt.axis('equal')
    plt.show()
    
spyral(0.1)

def A_spyral(k=0.1):
    fi = np.arange(0, 24, 0.1)
    r = k * fi
    x = r * sin(fi)
    y = r * cos(fi)
    plt.plot(x, y)
    plt.axis('equal')
    plt.show()
A_spyral()  

def wand(k=0.01):
    fi = np.arange(24, 0.1, -0.1)
    r = k / sqrt(fi)
    x = x = r * sin(fi)
    y = r * cos(fi)
    plt.plot(x, y)
    plt.axis('equal')
    plt.show()
wand()

def rose(k=5.5):
    fi = np.arange(0.1, 24, 0.1)

    r = sin(k * fi)
    x = r * sin(fi)
    y = r * cos(fi)
    plt.plot(x, y)
    plt.axis('equal')
    plt.show()
rose()
    
    

