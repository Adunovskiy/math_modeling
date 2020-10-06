a = int(input("Введите число: "))
while a > 0:
    b = a % 10
    a = a // 10
    print(b, end = "")
