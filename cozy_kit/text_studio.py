import string


class TextStudio:

    def to_morse(self, text):
        morse_code = {
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',

            '0': '-----',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',

            '.': '.-.-.-',
            ',': '--..--',
            '?': '..--..',
            '!': '-.-.--',
            '/': '-..-.',
            '(': '-.--.',
            ')': '-.--.-',
            ':': '---...',
            "'": '.----.',
            '=': '-...-',
            '+': '.-.-.',
            '-': '-....-',
            ' ': '/'
        }

        result = ''

        for letter in text.upper():
            result += f"{morse_code.get(letter, '?')} "

        return result.strip()

    def to_upper(self, text):
        return text.upper()

    def to_title(self, text):
        return text.title()

    def to_lower(self, text):
        return text.lower()

    def replace_with_spaces(self, text, replacement):
        return text.replace(replacement, ' ')

    def space_out_letters(self, text):
        result = ''

        for char in text:
            result += f'{char} '

        return result.strip()

    def reverse(self, text):
        return text[::-1]

    def word_count(self, text):
        return len(text.split())

    def char_count(self, text):
        return len(text)

    def remove_spaces(self, text):
        return text.replace(' ', '')

    def snake(self, text):
        return text.lower().replace(' ', '_')

    def caesar(self, text, shift):
        result = ''

        for char in text:
            if char.isalpha():

                start = ord('A') if char.isupper() else ord('a')

                shifted = (
                    (ord(char) - start + shift) % 26
                ) + start

                result += chr(shifted)

            else:
                result += char

        return result

    def remove_punctuation(self, text):
        result = ''

        for char in text:
            if char not in string.punctuation:
                result += char

        return result
