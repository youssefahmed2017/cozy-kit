import time
import math

from cozy_kit import errors


class CozyUI:
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
        self.TIME_TYPES = {"sec": 1, "min": 60, "hour": 3600}

    def __is_empty_text(self, text) -> None:
        if text == "":
            raise errors.EmptyTextError("Please enter text in the function parameters.")

    def __format_type(
        self,
        count: int,
        time_type: str,
    ) -> int:
        if time_type not in self.TIME_TYPES:
            raise errors.InvalidTimeTypeError(
                f'"{time_type}" is not a valid time type. ' "Choose: sec, min, or hour"
            )

        if not isinstance(count, int) or count < 0:
            raise errors.InvalidTimeAmountError(
                f'"{count}" is an invalid amount. '
                f"{count} must be greater than 0."
                f"And {count} must be a numerical number like 15."
            )

        count *= self.TIME_TYPES[time_type]

        return count

    def divider(self, symbol: str = "═", length: int = 30) -> str:
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

        length = math.floor(length / 2)

        self.__is_empty_text(text)

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

        self.__is_empty_text(headers)
        self.__is_empty_text(rows)

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

        progress_symbol = "█"
        percentage = percent // 10
        progress = progress_symbol * percentage

        if len(progress) < 10:
            progress += "-" * (10 - len(progress))

        return f"[{progress}] {percent}%"

    def cozy_box(
        self,
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

    def spinner(self, loadtime: int, load_type: str, style: str) -> str:
        """
        Displays an animated loading spinner.

        Parameters:
            loadtime:
                Spinner duration.

            load_type:
                sec, min, or hour.

            style:
                Spinner animation style.
        """

        SPINNER_FRAMES = {
            "line": ["|", "/", "-", "\\"],
            "dots": [".", "..", "...", "...."],
            "arrows": ["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"],
        }

        loadtime = self.__format_type(loadtime, load_type)

        frames = SPINNER_FRAMES.get(style, SPINNER_FRAMES["line"])
        frame_count = len(frames)
        start_time = time.time()
        interval = 0.03

        while True:
            elapsed = time.time() - start_time
            if elapsed >= loadtime:
                break

            index = int((elapsed / interval)) % frame_count
            print(f"\r{frames[index]}", end="", flush=True)
            time.sleep(interval)

        print("\rDone!", end="")
