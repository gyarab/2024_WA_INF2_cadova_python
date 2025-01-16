

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
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .')
    if any(char not in valid_chars for char in text):
        raise ValueError("Invalid character in text")
    encoded_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encoded_char = chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
            else:
                encoded_char = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
        elif char == ' ' or char == '.':
            encoded_char = char
        else:
            raise ValueError("Invalid character: " + char)
        encoded_text += encoded_char
    return encoded_text


def caesar_decode(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .')
    if any(char not in valid_chars for char in text):
        raise ValueError("Invalid character in text")
    decoded_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decoded_char = chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
            else:
                decoded_char = chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
        else:
            decoded_char = char
        decoded_text += decoded_char
    return decoded_text

def text_to_morse(text):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', 'Á' : '.-',  'Č': '-.-.',  'Ď': '-..', 'Ě': '.',  'É': '.', 'Í': '..', 'Ň': '-.', 'Ó': '---',
        'Ř': '.-.', 'Š': '...', 'Ť': '-', 'Ú': '..-', 'Ů': '..-', 'Ž': '--..', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
        'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
        'g': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
        'y': '-.--', 'z': '--..', 'á' : '.-',  'č': '-.-.',  'ď': '-..', 'ě': '.',  'é': '.', 'í': '..', 'ň': '-.', 'ó': '---',
        'ř': '.-.', 'š': '...', 'ť': '-', 'ú': '..-', 'ů': '..-', 'ž': '--..', ' ': '/'
    }
    morse_text = ""
    for char in text.upper():
        if char in morse_code:
            morse_text += morse_code[char] + " "
    return morse_text.strip()

if __name__ == "__main__":
    n = 3
    fib_number = fibonacci(n)
    print(fib_number)

   
    print(fib_number)

    print(is_prime(3))
    
    print(primes_in_range(1, 10))
    print(primes_in_range(10, 1))

    print(split_into_threes("Hello world!"))

    text = "Hello world."
    encodetext = caesar_encode(text)
    decodetext = caesar_decode(encodetext)
    print(encodetext)
    print(decodetext)

    print(text_to_morse("Ahoj světe!"))
