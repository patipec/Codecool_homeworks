def fibonacci():
    a = 0
    b = 1
    i = 0
    print(a)
    print(b)
    while i < 30:
        fib = a + b     
        print(fib)
        a = b
        b = fib
        i = i + 1
    return fib


fibo = fibonacci()
print(fibo)  
