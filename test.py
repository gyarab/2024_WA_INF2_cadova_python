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


if __name__ == "__main__":
    m = -1
    fib_number = fibonacci(m)
    print(fib_number)

    def is_prime(number):
        if number <= 0:
            raise ValueError("Number must be a natural number")
        
        if number == 1:
            return False
        
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        
        return True