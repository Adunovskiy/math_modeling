a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a == 0 or a == b:
    print("Одно из чисел равно нулю")
    
elif a % b == 0:
    print("Частное равно:", a // b)
    
elif a % b != 0:
    print("Частное равно:", a // b)
    print("Остаток равен:", a % b)