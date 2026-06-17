# ============= cozy_kit/text_studio.jpy =============

# ============= IMPORTS =============
import string

from cozy_kit import data
from cozy_kit._internal import errors
from cozy_kit._internal.helpers.text_helpers import TextHelpers

# ============= TextEditor CLASS =============


class TextEditor(TextHelpers):
    """
    Provides text formatting, transformation,
    and encoding utilities.

    Methods:
        to_morse(text)
        to_upper(text)
        to_lower(text)
        to_title()
        replace_with_spaces(text, replacement)
        space_out_letters(text)
        reverse(text)
        remove_spaces(text)
        snake_case(text)
        caesar_cipher(text, shift)
        pascal_case(text)
        kebab_case(text)
        word_count(text)
        char_count(text)
        count_vowels(text)
        corrupt(text, mode)
    """

    # ============= TEXT TRANSFORMATIONS =============
    def to_morse(self, text: str) -> str:
        """Converts text to Morse code.
        If text doesn't exist in Morse code, replaces it with '?'."""

        self._is_empty_text(text)

        result = ""

        for letter in text.upper():
            result += f"{data.morse_code.get(letter, '?')} "

        return result.strip()

    def to_upper(self, text: str) -> str:
        """Converts text to upper case."""

        self._is_empty_text(text)

        return text.upper()

    def to_title(self, text: str) -> str:
        """Converts text to title case."""

        self._is_empty_text(text)

        return text.title()

    def to_lower(self, text: str) -> str:
        """Converts text to lower case."""

        self._is_empty_text(text)

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

        self._is_empty_text(text)

        return text.replace(replacement, " ")

    def space_out_letters(self, text: str) -> str:
        """
        Adds a space after each letter
        in the text.
        """

        self._is_empty_text(text)

        result = "".join(f"{c} " for c in text).strip()

        return result.strip()

    def reverse(self, text: str) -> str:
        """Reverses the text."""

        self._is_empty_text(text)

        return text[::-1]

    def remove_spaces(self, text: str) -> str:
        """Removes spaces from the text."""

        self._is_empty_text(text)

        return text.replace(" ", "")

    def snake_case(self, text: str) -> str:
        """Converts text to snake case."""

        self._is_empty_text(text)

        return text.lower().replace(" ", "_")

    def caesar_cipher(
        self,
        text: str,
        shift: int,
    ) -> str:
        """
        Shifts each letter in the text
        using a Caesar cipher.
        Negative shifts are supported.
        """

        self._is_empty_text(text)

        if not isinstance(shift, int):
            raise errors.InvalidShiftError(
                f"{shift} is an invalid "
                "shift number. "
                f"{shift} must be an integer."
            )

        result = ""

        for char in text:
            if char.isalpha():
                start = ord("A") if char.isupper() else ord("a")

                shifted = ((ord(char) - start + shift) % 26) + start

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
        from the text
        including capital letters.
        """

        self._is_empty_text(text)

        result = "".join(c for c in text if c not in string.punctuation).lower()

        return result

    def pascal_case(self, text: str) -> str:
        """
        Converts text to PascalCase.
        """

        self._is_empty_text(text)

        result = text.title().replace(" ", "")

        return result

    def kebab_case(self, text: str) -> str:
        """
        Converts text to kebab-case.
        """

        self._is_empty_text(text)

        return text.lower().replace(" ", "-")

    def corrupt(self, text: str, mode: str) -> str:
        """
        Transforms text using a stylized corruption mode.

        Parameters:
            text: str
            mode:
                Corruption style.

        Available modes:
            glitch
            broken
            bubble
            void
        """

        self._is_empty_text(text)

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

    # ============= TEXT ANALYSIS =============

    def count_vowels(self, text: str) -> int:
        """
        Counts vowels in the text.
        """

        self._is_empty_text(text)

        result = 0

        for char in text.lower():
            if char in "aeiou":
                result += 1

        return result

    def word_count(self, text: str) -> int:
        """
        Returns the number of words
        in the text.
        """

        self._is_empty_text(text)

        return len(text.split())

    def char_count(self, text: str) -> int:
        """
        Returns the number of characters
        in the text.
        """

        self._is_empty_text(text)

        return len(text)


# ============= TextCustomizations CLASS =============


class TextCustomizations(TextHelpers):
    """
    Provides ANSI terminal text styling utilities.

    Supports:
        foreground colors
        background colors
        text effects
        combined ANSI styles
    Methods:
        customize(text, *styles)
    """

    def __init__(self):
        self.RESET = "\033[0m"

        self.ANSI_COLORS = {
            # Foreground colors
            "RED": "\033[31m",
            "GREEN": "\033[32m",
            "BLUE": "\033[34m",
            "YELLOW": "\033[33m",
            "CYAN": "\033[36m",
            "BLACK": "\033[30m",
            "MAGENTA": "\033[35m",
            "WHITE": "\033[37m",
            "GRAY": "\033[1;30m",
            # Background colors
            "RED_BG": "\033[41m",
            "GREEN_BG": "\033[42m",
            "BLUE_BG": "\033[44m",
            "YELLOW_BG": "\033[43m",
            "CYAN_BG": "\033[46m",
            "BLACK_BG": "\033[40m",
            "MAGENTA_BG": "\033[45m",
            "WHITE_BG": "\033[47m",
            # Bright colors
            "RED_BRIGHT": "\033[1;31m",
            "GREEN_BRIGHT": "\033[1;32m",
            "BLUE_BRIGHT": "\033[1;34m",
            "YELLOW_BRIGHT": "\033[1;33m",
            "CYAN_BRIGHT": "\033[1;36m",
            "BLACK_BRIGHT": "\033[1;30m",
            "MAGENTA_BRIGHT": "\033[1;35m",
            "WHITE_BRIGHT": "\033[1;37m",
            # Styles
            "BOLD": "\033[1m",
            "DIM": "\033[2m",
            "ITALIC": "\033[3m",
            "UNDERLINE": "\033[4m",
            "BLINK": "\033[5m",
            "REVERSE": "\033[7m",
            "HIDDEN": "\033[8m",
        }

    def customize(self, text: str, *styles: str) -> str:
        """
        Wrap text with ANSI styles/colors.

        Parameters:
            text: str
            *styles: str
        """

        self._is_empty_text(text)

        ansi = ""

        for style in styles:
            style = style.upper().replace(" ", "_")
            self._is_existing_style(style, self.ANSI_COLORS)
            key = style
            ansi += self.ANSI_COLORS.get(key, "")

        return f"{ansi}{text}{self.RESET}"
