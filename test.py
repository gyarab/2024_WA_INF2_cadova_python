print("Hello world!")
def fibonacci(n):
    if n < 0:
        raise ValueError("n cannot be negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b   
    return a

# Example usage


def is_prime(number):
    if number <= 0 or not isinstance(number, int):
        raise ValueError("Number must be a natural number")
        
    if number == 1:
        return False
    
    if number == 1.0:
        return False
        
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
        
    return True

def primes_in_range(a, b):
    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        raise ValueError("Invalid input. a and b must be non-negative integers")
        
    primes = []
    start = min(a, b)
    end = max(a, b)
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
        
    return primes

if __name__ == "__main__":
    n = 3
    fib_number = fibonacci(n)
    print(fib_number)

    m = -1
    fib_number = fibonacci(m)
    print(is_prime(0.3))

    print(fib_number)

    print(is_prime(3))
    
    print(primes_in_range(1, 10))
    print(primes_in_range(10, 1))
