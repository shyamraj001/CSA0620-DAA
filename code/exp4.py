def fibonacci_iterative(n):
    series = []
    a, b = 0, 1

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series


# Fibonacci Series - Recursive

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n = 6

print("Iterative:", fibonacci_iterative(n))

print("Recursive:", [fibonacci_recursive(i) for i in range(n)])
print("B.Shyam raj")
print("192421176")

