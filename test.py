print("Hello world!")
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b   
    return sequence

# Example usage
n = 8
fib_sequence = fibonacci(n)
print(fib_sequence)
