a = int(input("Введите число: "))
i = 1
j = 1
dels = []
while a >= i:
    if a % i == 0:
      dels.append(a // i)
      i = i + 1
    else:
        i = i + 1
print(dels)     

for i in dels:
    while i >= j:
        c = i % j 
        if c == 0:
            break
        j += 1
        
        
