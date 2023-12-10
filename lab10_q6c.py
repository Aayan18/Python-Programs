def fibonacci(n, a=0, b=1):
    if n > 0:
        print(a, end=" ")
        return fibonacci(n-1, b, a+b)
N = int(input('enter the value of N:'))
print(fibonacci(N))
