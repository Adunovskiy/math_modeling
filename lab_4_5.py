import numpy as np
def square(a=1, b=1, r=1):
    square = 0
    print("Выберите фигуру: 1 - прямоугольник, 2 - круг, 3 - треугольник")
    figure = int(input("Введите номер фигуры: "))
    if figure == 1:
        a = int(input("Введите длину: "))
        b = int(input("Введите ширину: "))
        square = a * b
    elif figure == 2:
        r = int(input("Введите радиус: "))
        square = np.pi * r ** 2
    elif figure == 3:
        a = int(input("Введите длину первого катета: "))
        b = int(input("Введите длину второго катета: "))
        square = a * b * 0.5
    else:
        print("Выбран неверный номер фигуры")        
    print("S =", square, "cm")
square(1, 2)
