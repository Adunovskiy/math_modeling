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
    
            
            
        
def func_new(x):
    a = int(input("Введите начало ОДЗ: "))
    b = int(input("Введите конец ОДЗ: "))
    x = np.arange(a, b, 0.1)
    y = 4 * x + 3
    print(y)
    
func(1)
