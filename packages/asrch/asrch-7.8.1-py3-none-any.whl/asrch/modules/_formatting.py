"""
Formatting module for asrch
"""

import re
import shutil
from typing import Optional

from asrch.utils.constants import Colors

colors = Colors()
terminal_size = round(shutil.get_terminal_size().columns)


class Bar:
    """
    Bar class to create bar object
    """

    @staticmethod
    def bar(
        char: str,
        title: str,
        t_color: Optional[Colors | str],
        bg_color: Optional[Colors | str],
    ) -> str:
        """
        :param char: The character used to represent the bar
        :type char: str

        :param title: The title of the bar
        :type title: str

        :param title_color: The color of the title. Can be a Colors type or a string representing
        a color.
        :type title_color: BarColor | str

        :param background_color: The background color of the bar. Can be a BarColor enum or a
        string representing a color.
        :type background_color: Color | str
        """

        terminal_size = round(shutil.get_terminal_size().columns)
        bar_array: list[str] = []

        title = f"{t_color}{title:^{round(terminal_size)}}{bg_color}"
        if len(char) < 1:
            raise ValueError("Char must be 1 character long")

        for _ in range(terminal_size):
            bar_array.append(char)
        formatted_array = (
            str(bar_array)
            .replace("'", "")
            .replace(",", "")
            .replace(" ", "")
            .replace("[", "")
            .replace("]", "")
        )
        if bg_color is None and t_color is None:
            return f"{formatted_array}\
\n{title:{char}^{round(terminal_size)}}\
\n{formatted_array}".replace("None", "")
        else:
            return f"{bg_color}{formatted_array}\
\n{title:{char}^{round(terminal_size)}}{Colors.NC}\
\n{bg_color}{formatted_array}{Colors.NC}"


class Highlighter:
    """
    Highlighter class for methods regarding string formatting
    """

    @staticmethod
    def highlight_html(text: str) -> str:
        """
        Highlight certain keywords to make output more readable

        :param text: The string to highlight
        :type text str
        """

        text = re.sub(r"var", rf"{Colors.ORANGE}", text)
        text = re.sub(r"function", rf"{Colors.ORANGE}", text)
        text = re.sub(r"\d+", rf"{Colors.GREEN}", text)
        return text

    @staticmethod
    def highlight_page_output(text: str) -> str:
        """
        Highlight certain keywords to make output more readable

        :param text: The string to highlight
        :type text: str
        :return: The string with highlighted keywords
        :rtype: str
        """

        # Define color escape sequences or color codes
        colors = {
            "URL": Colors.DIM_GRAY,
            "HEADER": Colors.PASTEL_BLUE,
            "CODE": Colors.PASTEL_GREEN,
            "COMMAND": "\x1b[48;5;238m",
            "NUMBER": Colors.PASTEL_CYAN,
        }

        # Replace URLs
        """text = re.sub(
            r"https?://\S+",
            lambda match: f"{colors['URL']}{match.group(0)}\x1b[0m",
            text,
        )"""

        # Highlight headers
        text = re.sub(
            r"(#+)\s*(.*?)\s*(#+)*",
            lambda match: f"{colors['HEADER']}{match.group(1)}{match.group(2)}{match.group(3) if match.group(3) else ''}\x1b[0m",
            text,
        )

        # Highlight code snippets (assuming they are in backticks)
        text = re.sub(
            r"`(.*?)`",
            lambda match: f"{colors['CODE']}`{match.group(1)}`\x1b[0m",
            text,
        )

        text = re.sub(
            r"^(>>> .*)$",
            lambda match: f"{colors['COMMAND']}{match.group(1)}\x1b[0m",
            text,
            flags=re.MULTILINE,
        )

        return text

    @staticmethod
    def highlight_nums(text: str) -> str:
        # Define ANSI escape codes for bold pink text
        ANSI_BOLD_PINK = "\033[1;95m"
        ANSI_RESET = "\033[0m"

        # Regex pattern to find numbers (including decimals and negative signs)
        pattern = r"[-+]?\d*\.\d+|\d+"

        # Replace all matches with bold pink text
        highlighted_text = re.sub(pattern, f"{ANSI_BOLD_PINK}\\g<0>{ANSI_RESET}", text)

        return highlighted_text


class Text:
    def print_centered(text, terminal_width=80):
        # Split text into lines
        lines = text.splitlines()

        # If there are no lines, return an empty string
        if not lines:
            return ""

        # Calculate left indent to center the text
        left_indent = (terminal_width - max(len(line) for line in lines)) // 2

        # Center each line within terminal width
        centered_lines = [line.center(terminal_width) for line in lines]

        # Join centered lines with newline characters and return as a single string
        centered_text = "\n".join(centered_lines)

        return centered_text

    def print_indented(text, indentation="\t\t"):
        lines = text.splitlines()
        new_output = []
        i = 0
        for line in lines:
            i += 1
            formatted_line = line
            formatted_line = f"{i}│{line}"
            new_output.append(formatted_line)

        indented_text = "\n".join(new_output)
        return indented_text
