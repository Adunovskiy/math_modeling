a = int(input('Введите длину ряда Фибоначи: '))
for i in range (a):
    if i == 0:
        print(i + 1)
        c = 1
    elif i == 1:
        print(i)
        b = 1
    else:
        d = b + c
        print(d)
        b = d

       
        
    
    
    