
# Making a class for the errors
class MorseError(Exception):
    pass

# A dictinary to link between each letter and its morse
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

# Making a function to turn from text to morse
def text_to_morse(text):
    text = text.upper()  # converting the text into upper case
    result = []
    for char in text:
        if char in MORSECODE:
            result.append(MORSECODE[char])  # Append Morse code for the character
        elif char == " ":
            result.append("/")  # Append space for space in the input
        else:
            raise MorseError(f"The '{char}' key doesn't exist in the dictionary")  # Raise an error if the character is not in the dictionary
    return ' '.join(result)  # Join Morse code representations with spaces between characters

# making a function to convert from morse to text
def morse_to_text(morse_code):
    morse_words = morse_code.split('/')  # Split Morse code by '/'
    result = []
    for morse_word in morse_words:
        morse_chars = morse_word.strip().split()  # Split Morse word into Morse characters
        for char in morse_chars:
            # comparing the morse to the values
            for key, value in MORSECODE.items():
                if value == char:
                    result.append(key)  # Appending the key "english character" of the value
                    break
            else:
                # If Morse code is not found in the dictionary
                if char == "":
                    result.append(" ")  # Handle space between words
                else:
                    raise MorseError(f"The Morse code '{char}' is not in the dictionary")  # Raise an error if the Morse code is not in the dictionary
        result.append(" ")  # Add space between words
    return ''.join(result).strip()  # Remove trailing spaces

# Function for user interaction
def choosinginput():
    # Ask the user for their choice
    choice = input("Press 'english' for English to Morse code or 'morse' for Morse code to English: ").lower()

    # Check the user's choice
    if choice == "english":
        string = input("Enter text: ")
        print(text_to_morse(string))  # Call the function to convert English to Morse code
    elif choice == "morse":
        string = input("Enter Morse code (use '.' or '-' , space between characters and '/' between words): ")
        print(morse_to_text(string))  # Call the function to convert Morse code to English
    else:
        print("Choose only between english or morse.")  # Print an error message for an incorrect choice

#calling the function to getting the user's input
choosinginput()


