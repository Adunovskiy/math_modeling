i = 5
while i < 15:
    print(i)
    i = i + 2

for i in 'Hello world':
    if i == 'o':
        break
    print(i * 2, end = ' ')

for i in 'Hello world':
    if i == 0:
        continue
    print(i * 2, end= ' ')