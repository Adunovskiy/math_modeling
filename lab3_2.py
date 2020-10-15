import numpy as np
import lab3_1 as const
b = 30
a = np.pi / 3
h = 100
v = np.sqrt((const.g * h * np.tan(b) ** 2 ) / (2 * np.cos(a) ** 2 * (1 - np.tan(b) * np.tan(a))))
print(v)

from lab3_1 import k, e, h 
t = 200
epsilon = 300
n = (2 / np.sqrt(np.pi)) * (h / (k * t) ** (3/2) * e ** ((epsilon * (-1)) / (k * t)) * epsilon ** (t /2) )
print(n)