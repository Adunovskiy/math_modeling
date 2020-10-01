a = int(input('Введите первый член прогрессии: '))
b = int(input('Введите знаменатель прогрессии: '))
c = int(input('Введите количество членов прогрессии: '))
print(a)
for i in range (c):
    print(a * b)
    a = a * b