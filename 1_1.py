###### Ввод ######

import random

n = int(input()) # Длина массива
mass = []
x = []

###### Заполнение массива ######

for i in range(n):
    mass.append(random.random)
    
###### Программа ######

for i in range(n):
    a1 = 1
    a2 = 1
    a3 = 1
    if i > 0:
        x.append(a1)
        for i in range(n):
            x.append(a3)
            a3 = a1+a2
            a1 = a2
            a2 = a3
print(x)
