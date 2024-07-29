import time
import sys
import shutil
from contextlib import contextmanager
from ascli.modules._alert import Alert
from ascli.modules._output import clear_last_lines, move_cursor_to_bottom, save_cursor_position, restore_cursor_position
from asrch.modules._formatting import Bar
from asrch.utils.constants import Colors

colors = Colors()
form = Bar()


@contextmanager
def format_bars(bar_char, message, color_start, color_end):
    start_time = time.time()
    print(form.bar(bar_char, "START " + message, color_start, colors.TIME))
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(
        form.bar(
            bar_char,
            f"END {message} (Time: {elapsed_time:.2f} seconds)",
            color_end,
            colors.TIME,
        )
    )


@contextmanager
def format_alerts(delay, msg):
    print("\033[H\033[2J")
    start_time = time.time()
    Alert.alert(delay=delay,msg=msg)
    print()
    yield
    print()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("\033[H\033[2J")
    Alert.alert(delay=delay+3,msg=f"Done ({elapsed_time})")
    print("\033[H\033[2J")

