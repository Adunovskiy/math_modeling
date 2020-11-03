def extent(a=1, n=1):
    a1 = a
    i = 1
    while i < n:
        a = a1 * a
        i += 1
    print(a)
extent(2, 4)