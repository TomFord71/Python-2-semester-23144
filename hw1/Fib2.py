def fib(n):
    a = 1
    b = 0
    res = 0
    for i in range(n):
        res = a + b
        b = a
        a = res
    return res

n = int(input())
print(fib(n))