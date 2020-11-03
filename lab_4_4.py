def func(x):
    y = 0
    posx = []
    posy = []
    a = int(input("Введите начало ОДЗ: "))
    b = int(input("Введите конец ОДЗ: "))
    if x > a and x < b:
        while x > a and x < b:
            y = 4 * x + 3
            posy.append(y)
            posx.append(x)
            x += 1
        print(posx)
        print(posy)
    else:
        print("Неверное значение аргумента")
func(1)
    
            
            
        