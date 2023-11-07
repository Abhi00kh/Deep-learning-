def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

# Example usage
n = 10  # Change this value to calculate Fibonacci series up to a different number
print("Recursive Fibonacci Series:")
for i in range(n):
    print(recursive_fibonacci(i))


def non_recursive_fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) <=n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Example usage
n = 10  # Change this value to calculate Fibonacci series up to a different number
print("Non-Recursive Fibonacci Series:")
print(non_recursive_fibonacci(n))
