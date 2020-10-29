a = []
N = 5
for i in range(N):
    num = int(input())
    a.append(num)
print(a)
num = int(input("Введите число: "))
j = int(input("Введите позицию: "))
 
a = a[0:j-1] + [num] + a[j-1:]
 
print(a)