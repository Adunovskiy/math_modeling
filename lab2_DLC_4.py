a = int(input("Введите число: "))
i = 1
for i in range (1, a, 1):
    i = a // i
    i = i + 1 
    print(i, end = ' ')