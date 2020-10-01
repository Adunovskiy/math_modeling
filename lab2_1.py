a = int(input('Введите число: '))
if a % 2 == 0 and a != 0:
    print('Чётное')
elif a % 2 != 0 and a != 0:
    print('Нечётное')
else:
    print('Что-то там')