# ============= cozy_kit/ui.py =============

# ============= IMPORTS =============

import time
import asyncio

from cozy_kit import TextCustomizations
from cozy_kit._internal import errors


# ============= CozyUI CLASS =============
class CozyUI(TextCustomizations):
    """
    Provides terminal UI utilities and animations.

    Includes:
        - tables
        - dividers
        - loading spinners
        - progress bars
        - terminal boxes
    """

    def __init__(self) -> None:
        super().__init__()
        self.TIME_TYPES = {"sec": 1, "min": 60, "hour": 3600}
        self.SPINNER_FRAMES = {
            "line": ["|", "/", "-", "\\"],
            "dots": [".  ", ".. ", "...", "   "],
            "arrows": ["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"],
        }

    def _convert_type_to_seconds(
        self,
        count: int,
        time_type: str,
    ) -> int:
        """
        Converts a time amount into seconds.

        Parameters:
            count:
                Time amount.

            time_type:
                sec, min, or hour.

        Returns:
            int:
                Time converted to seconds.
        """
        # Check if time_type and count are not right
        if time_type not in self.TIME_TYPES:
            raise errors.InvalidTimeTypeError(
                f'{time_type}" is not a valid time type. ' "Choose: sec, min, or hour"
            )

        if count <= 0:
            raise errors.InvalidTimeAmountError(
                f'{count}" is an invalid amount. ' f"{count} must be greater than 0"
            )

        count *= self.TIME_TYPES[time_type]

        return count

    @staticmethod
    def divider(symbol: str = "═", length: int = 30) -> str:
        """
        Creates a divider line using a repeated symbol.
        """

        return symbol * length

    def cozy_title(
        self,
        text: str,
        symbol: str = "═",
        length: int = 15,
    ) -> str:
        """
        Creates a centered terminal title.

        Parameters:
            text:
                Title text.

            symbol:
                Border symbol.

            length:
                Total border length.

        Returns:
            Formatted title string.
        """

        length = length // 2

        self._is_empty_text(text)

        return f"{symbol * length} {text} {symbol * length}"

    def cozy_table(
        self,
        headers: list[str],
        rows: list[list[str]],
    ) -> str:
        """
        Creates a formatted terminal table.

        Parameters:
            headers:
                Table headers.

            rows:
                Table rows.

        Returns:
            Formatted table string.
        """

        self._is_empty_text(headers)
        self._is_empty_text(rows)

        column_widths = []

        for column_index in range(len(headers)):
            max_width = len(headers[column_index])

            for row in rows:
                cell_length = len(str(row[column_index]))

                if cell_length > max_width:
                    max_width = cell_length

            column_widths.append(max_width)

        top_border = "╔"
        middle_border = "╠"
        bottom_border = "╚"

        for i, width in enumerate(column_widths):
            top_border += "═" * (width + 2)
            middle_border += "═" * (width + 2)
            bottom_border += "═" * (width + 2)

            if i < len(column_widths) - 1:
                top_border += "╦"
                middle_border += "╬"
                bottom_border += "╩"

        top_border += "╗"
        middle_border += "╣"
        bottom_border += "╝"

        header_row = "║"

        for i, header in enumerate(headers):
            header_row += f" {header.ljust(column_widths[i])} ║"

        table_rows = ""

        for row in rows:
            table_rows += "║"

            for i, cell in enumerate(row):
                table_rows += f" {str(cell).ljust(column_widths[i])} ║"

            table_rows += "\n"

        return (
            f"{top_border}\n"
            f"{header_row}\n"
            f"{middle_border}\n"
            f"{table_rows}"
            f"{bottom_border}"
        )

    def progress_bar(self, percent: int) -> str:
        """
        Creates a terminal progress bar.

        Parameters:
            percent:
                Progress percentage.

        Returns:
            Formatted progress bar.
        """

        filled = percent // 10
        empty = 10 - filled

        return f"""{self.customize(f'{"━" * filled}', "blue", "bold")} {self.customize(f"{'━' * empty}", 'red', 'bold')} {percent}%"""

    @staticmethod
    def cozy_box(
        text: str,
    ) -> str:
        """
        Creates a terminal box around text.

        Parameters:
            text:
                Text inside the box.

        Returns:
            Box-formatted string.
        """

        border = "═" * (len(text) + 2)

        return f"╔{border}╗\n" f"║ {text} ║\n" f"╚{border}╝"

    def spinner(
        self,
        loadtime: int,
        load_type: str = "sec",
        style: str = "dots",
        message: str = "Loading",
    ) -> None:
        """
        Displays an animated loading spinner.

        Parameters:
            loadtime:
                Spinner duration.

            load_type:
                sec, min, or hour.

            style:
                Spinner animation style.

            message:
                The message to show where the spinner will animate through it.
                e.g. Loading... (The three dots are the spinner and Loading is the message.)
        """

        loadtime = self._convert_type_to_seconds(loadtime, load_type)

        frames = self.SPINNER_FRAMES.get(style, self.SPINNER_FRAMES["line"])
        frame_count = len(frames)
        start_time = time.time()
        interval = 0.03

        while True:
            elapsed = time.time() - start_time

            if elapsed >= loadtime:
                break

            index = int(elapsed / interval) % frame_count

            print(f"\r{message}{frames[index]}", end="", flush=True)

            time.sleep(interval)

        print(f"\r{message} | Done!")

    async def async_spinner(
        self, loadtime: int, load_type: str, style: str, message: str
    ) -> None:
        """Displays an animated spinner using async instead of time.sleep.
        Parameters:
            loadtime: int
            load_type: str
            style: str
            message: str
        """
        loadtime = self._convert_type_to_seconds(loadtime, load_type)

        frames = self.SPINNER_FRAMES.get(style, self.SPINNER_FRAMES["line"])

        frame_count = len(frames)

        start_time = time.time()

        interval = 0.03

        while True:
            elapsed = time.time() - start_time

            if elapsed >= loadtime:
                break

            index = int(elapsed / interval) % frame_count

            print(f"\r{message}{frames[index]}", end="", flush=True)

            await asyncio.sleep(interval)

        print("\tDone!")
