# Define custom exceptions for Morse code conversion errors
class MorseError(Exception):
    pass

# Define the Morse code mappings for English letters, numbers, and symbols
MORSECODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
    'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Define a function to convert English text to Morse code
def text_to_morse(text):
    text = text.upper()  # Convert input to uppercase
    result = []
    for char in text:
        if char in MORSECODE:
            result.append(MORSECODE[char])  # Append Morse code for the character
        elif char == " ":
            result.append("/")  # Append space for space in the input
        else:
            raise MorseError(f"The '{char}' key doesn't exist in the dictionary")  # Raise an error if the character is not recognized
    return ' '.join(result)  # Join Morse code representations with spaces between characters