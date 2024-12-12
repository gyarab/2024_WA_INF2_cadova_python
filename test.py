print("Hello world!")
def fibonacci(n):
    if n < 0:
        raise ValueError("n cannot be negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b   
    return a

# Example usage
n = 3
fib_number = fibonacci(n)
print(fib_number)

m = -1
fib_number = fibonacci(m)
print(fib_number)
