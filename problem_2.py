def fib(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

print(sum(x for x in fib(4000000) if x % 2 == 0))
