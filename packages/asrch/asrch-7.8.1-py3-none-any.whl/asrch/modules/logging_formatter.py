import logging
from inspect import stack
from pathlib import Path

from asrch.modules._formatting import Highlighter
from asrch.utils.constants import Colors, Files

current_file = Files()

highlight_text = Highlighter()
color = Colors()
nc = color.NC
h = ""


class ColorFormatter(logging.Formatter):
    def __init__(self, fmt):
        super().__init__()
        fmt = fmt.split("|")
        self.FORMATS = {
            logging.DEBUG: f"{color.DIM_GRAY}{color.GRAY}{Path(stack()[1].filename).name:<22}↪{color.TIME}{fmt[0]}{color.NC}{color.YELLOW}{fmt[1]}{color.DIM_GRAY}{h:<4}%(lineno)d↪ {nc}{fmt[2]} {nc}",
            logging.INFO: f"{color.DIM_GRAY}{color.GRAY}{Path(stack()[1].filename).name:<22}↪{color.TIME}{fmt[0]}{color.NC}{color.BLUE}{fmt[1]}{color.DIM_GRAY}{h:<4}%(lineno)d↪ {nc}{fmt[2]} {color.NC}",
            logging.WARNING: f"{color.DIM_GRAY}{color.GRAY}{Path(stack()[1].filename).name:<22}↪{color.TIME}{fmt[0]}{color.NC}{color.ORANGE}{fmt[1]}{color.DIM_GRAY}{h:<4}%(lineno)d↪ {nc}{fmt[2]} {color.NC}",
            logging.ERROR: f"{color.DIM_GRAY}{color.GRAY}{Path(stack()[1].filename).name:<22}↪{color.TIME}{fmt[0]}{color.NC}{color.RED}{fmt[1]}{color.DIM_GRAY}{h:<4}%(lineno)d↪ {nc}{fmt[2]} {color.NC}",
            logging.CRITICAL: f"{color.DIM_GRAY}{color.GRAY}{Path(stack()[1].filename).name:<22}↪{color.TIME}{fmt[0]}{color.NC}{color.CRITICAL}{fmt[1]}{color.DIM_GRAY}{h:<4}%(lineno)d↪ {nc}{fmt[2]} {color.NC}",
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
