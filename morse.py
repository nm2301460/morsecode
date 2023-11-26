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

# Define a function to convert Morse code to English text
def morse_to_text(morse_code):
    morse_words = morse_code.split('/')  # Split Morse code by '/'
    result = []
    for morse_word in morse_words:
        morse_chars = morse_word.strip().split()  # Split Morse word into Morse characters
        for char in morse_chars:
            # Lookup the Morse code directly in the MORSECODE dictionary
            for key, value in MORSECODE.items():
                if value == char:
                    result.append(key)  # Append English character for the Morse code
                    break
            else:
                # If Morse code is not found in the dictionary
                if char == "":
                    result.append(" ")  # Handle space between words
                else:
                    raise MorseError(f"The Morse code '{char}' doesn't exist in the dictionary")  # Raise an error if the Morse code is not recognized
        result.append(" ")  # Add space between words
    return ''.join(result).strip()  # Remove trailing spaces