def fib(n: int) -> int:
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


n = 4
print(f"{n}th Element of the Fibonacci Series:", fib(n))
