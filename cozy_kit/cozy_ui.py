from cozy_kit import errors

class CozyUI:
    def __is_empty_text(self, text):
        if text == "":
            raise errors.EmptyTextError('Please enter text in the function parameters.')

    def divider(
            self,
            symbol:str = '═',
            length: int = 30
    ) -> str:
        return symbol * length

    def cozy_title(
            self,
            text: str,
            symbol: str = '═',
            length: int = 15,
    ):
        self.__is_empty_text(text)

        return f"{symbol * length} {text} {symbol * length}"

    def cozy_table(
            self,
            headers: list[str],
            rows: list[list[str]],
    ) -> str:
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
                table_rows += (
                    f" {str(cell).ljust(column_widths[i])} ║"
                )

            table_rows += "\n"

        return (
            f"{top_border}\n"
            f"{header_row}\n"
            f"{middle_border}\n"
            f"{table_rows}"
            f"{bottom_border}"
        )

    def progress_bar(
            self,
            percent: int
    ) -> str:
        progress_symbol = '█'
        percentage = percent // 10
        progress = progress_symbol * percentage

        if len(progress) < 10:
            progress += "-" * (10 - len(progress))

        return f'[{progress}] {percent}%'

    def cozy_box(
            self,
            text: str,
    ) -> str:
        """Creates a cool box around the text.
        Only supports single line"""
        border = "═" * (len(text) + 2)

        return (
            f"╔{border}╗\n"
            f"║ {text} ║\n"
            f"╚{border}╝"
        )
