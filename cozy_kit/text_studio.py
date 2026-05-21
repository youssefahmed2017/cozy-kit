import string

from . import data, errors

"""
Text utility module.

Features:
    - morse code conversion
    - upper case conversion
    - title case conversion
    - lower case conversion
    - replacing text with spaces
    - spacing out letters
    - reversing text
    - word counting
    - character counting
    - punctuation removal
    - space removal
    - snake case conversion
    - Caesar cipher support
"""


class TextStudio:
    def __is_empty_text(self, text):
        if text == "":
            raise errors.EmptyTextError('Please enter text in the function parameters.')

    def to_morse(
            self,
            text: str
    ) -> str:
        """Converts text to Morse code.
        If text doesn't exist in Morse code, replaces it with '?'."""
        self.__is_empty_text(text)

        result = ""

        for letter in text.upper():
            result += (
                f"{data.morse_code.get(letter, '?')} "
            )

        return result.strip()

    def to_upper(self, text: str) -> str:
        """Converts text to upper case."""
        self.__is_empty_text(text)

        return text.upper()

    def to_title(self, text: str) -> str:
        """Converts text to title case."""
        self.__is_empty_text(text)

        return text.title()

    def to_lower(self, text: str) -> str:
        """Converts text to lower case."""
        self.__is_empty_text(text)

        return text.lower()

    def replace_with_spaces(
        self,
        text: str,
        replacement: str,
    ) -> str:
        """
        Replaces the given replacement
        with spaces in the text.
        """
        self.__is_empty_text(text)

        return text.replace(replacement, " ")

    def space_out_letters(self, text: str) -> str:
        """
        Adds a space after each letter
        in the text.
        """
        self.__is_empty_text(text)

        result = "".join(f"{c} " for c in text).strip()

        return result.strip()

    def reverse(self, text: str) -> str:
        """Reverses the text."""
        self.__is_empty_text(text)

        return text[::-1]

    def word_count(self, text: str) -> int:
        """
        Returns the number of words
        in the text.
        """
        self.__is_empty_text(text)

        return len(text.split())

    def char_count(self, text: str) -> int:
        """
        Returns the number of characters
        in the text.
        """
        self.__is_empty_text(text)

        return len(text)

    def remove_spaces(self, text: str) -> str:
        """Removes spaces from the text."""
        self.__is_empty_text(text)

        return text.replace(" ", "")

    def snake(self, text: str) -> str:
        """Converts text to snake case."""
        self.__is_empty_text(text)

        return text.lower().replace(" ", "_")

    def caesar(
        self,
        text: str,
        shift: int,
    ) -> str:
        """
        Shifts each letter in the text
        using a Caesar cipher.
        Negative shifts are supported.
        """
        self.__is_empty_text(text)

        if not isinstance(shift, int):
            raise errors.InvalidShiftError(
                f"{shift} is an invalid "
                "shift number. "
                f"{shift} must be an integer."
            )

        result = ""

        for char in text:
            if char.isalpha():
                start = (
                    ord("A")
                    if char.isupper()
                    else ord("a")
                )

                shifted = (
                    (ord(char) - start + shift)
                    % 26
                ) + start

                result += chr(shifted)

            else:
                result += char

        return result

    def remove_punctuation(
        self,
        text: str,
    ) -> str:
        """
        Removes punctuation
        from the text.
        """
        self.__is_empty_text(text)

        result = "".join(c for c in text if c not in string.punctuation)

        return result

    def pascal_case(
            self,
            text: str
    ) -> str:
        self.__is_empty_text(text)

        result = text.title().replace(" ", "")
        return result

    def kebab_case(
            self,
            text: str
    ) -> str:
        self.__is_empty_text(text)

        # FIX 1: Was missing return, and used .title() — kebab-case should be lowercase
        return text.lower().replace(" ", "-")

    # FIX 2+3: Return type was str (should be int); logic checked if 'aeiou' as a whole string
    # exists in text instead of checking each character individually
    def count_vowels(
        self,
        text: str
    ) -> int:
        self.__is_empty_text(text)

        result = 0

        for char in text.lower():
            if char in 'aeiou':
                result += 1

        return result

    def corrupt(
            self,
            text: str,
            mode: str
    ) -> str:

        self.__is_empty_text(text)

        result = ""

        for char in text.lower():

            if mode == "glitch":
                result += data.GLITCH_MODE.get(char, char)

            elif mode == "broken":
                result += data.BROKEN_MODE.get(char, char)

            elif mode == "bubble":
                result += data.BUBBLE_MODE.get(char, char)

            elif mode == "void":
                result += data.VOID_MODE.get(char, char)

            else:
                result += char

        return result