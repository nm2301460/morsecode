import unittest
from morsep import text_to_morse, morse_to_text, MorseError

class TestMorseConversion(unittest.TestCase):

    def test_text_to_morse(self):
        self.assertEqual(text_to_morse("HELLO WORLD"), ".... . .-.. .-.. --- / .-- --- .-. .-.. -..")
        self.assertEqual(text_to_morse(""), "")
        self.assertEqual(text_to_morse("help!?!"), ".... . .-.. .--. -.-.-- ..--.. -.-.--")
        self.assertEqual(text_to_morse("123"), ".---- ..--- ...--")

    def test_morse_to_text(self):
        self.assertEqual(morse_to_text(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."), "HELLO WORLD")
        self.assertEqual(morse_to_text(""), "")
        self.assertEqual(morse_to_text(".... . .-.. .--. -.-.-- ..--.. -.-.--"), "HELP!?!")
        self.assertEqual(morse_to_text(".---- ..--- ...--"), "123")

    def test_invalid_text_to_morse(self):
        with self.assertRaises(MorseError):
            text_to_morse("#Invalid#")

    def test_invalid_morse_to_text(self):
        with self.assertRaises(MorseError):
            morse_to_text(".... . .-.. .-.. --- / .-- --- .-. .-.. -.. #Invalid#")

if __name__ == '__main__':
    unittest.main()
