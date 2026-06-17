# ============= cozy_kit/_internal/helpers/text_helpers.py =============

from cozy_kit._internal import errors


class TextHelpers:
    @staticmethod
    def _is_empty_text(text) -> None:
        if not text:  # Check if text is not empty
            raise errors.EmptyTextError("Please enter text in the function parameters.")

    @staticmethod
    def _is_existing_style(style: str, ansi_colors: dict) -> None:
        if (
            style not in ansi_colors
        ):  # Check if the style exists in the ANSI_COLORS dictionary
            raise errors.InvalidStyleError(
                f"You entered an invalid style: {style}. "
                f"\nPlease enter one of these styles:\n "
                f"{ansi_colors.keys()}"
            )
