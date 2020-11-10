def fib(n):
    fib = 0
    if n >= 0:
        temp = 0
        temp1 = 1
        for i in range(n):
            fib = fib + temp
            temp = fib + temp1
            temp1 = temp + fib
        print(fib)
fib()
     