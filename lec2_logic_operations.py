a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))

if a > 4 and b == 2: # and - операция логического "И"
    print('Good')
elif b > 3 or c == 5:
    print('Best') # or - операция логического "ИЛИ"
else:
    print('Bad')
    