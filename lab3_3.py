from lab3_1 import g
import numpy as np
pos = []
x = 0
y = 0
x0 = 0
y0 = 0
i = 0
t = 0
v = int(input('Введите скорость: '))
while t <= 5:
    x = x0 + v * t
    y = y0 + v * t - g * t ** 2 / 2
    pos.append(t)
    pos.append(x)
    pos.append(y)
    print(pos)
    pos = []
    t += 0.1
    
    