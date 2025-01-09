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

def split_into_threes(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
            
    result = []
    for i in range(0, len(text), 3):
        result.append(text[i:i+3])
            
    return result

def caesar_encode(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    encoded_text = ""
    for char in text:
        if not char.isalpha():
            raise ValueError("Input must contain only letters")
        
        if char.isupper():
            encoded_char = chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
        else:
            encoded_char = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
        encoded_text += encoded_char
    return encoded_text

def caesar_decode(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    decoded_text = ""
    for char in text:
        if not char.isalpha():
            raise ValueError("Input must contain only letters")
        
        if char.isupper():
            decoded_char = chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
        else:
            decoded_char = chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
        decoded_text += decoded_char
    return decoded_text

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

    print(split_into_threes("Hello world!"))

    text = "Hello world!"
    print(caesar_encode(text))
    print(caesar_decode(text))
