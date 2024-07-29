"""
Constants
"""

from enum import Enum
from pathlib import Path


class OpenModes(Enum):
    """
    Modes for the open command
    """

    TEXT = "text"
    BODY = "body"
    JS = "js"
    HTML = "html"
    IMG = "img"
    SS = "ss"
    INS = "inspect"


class Colors:
    # Main stuff
    GREEN = "\x1b[38;5;40m"
    RED = "\x1b[38;5;196m"
    ORANGE = "\x1b[38;5;202m"
    YELLOW = "\x1b[38;5;226m"
    BLUE = "\x1b[38;5;21m"
    NC = "\x1b[0m"
    GRAY = "\x1b[38;5;243m"
    MAGENTA = "\x1b[45m"
    DIM_GRAY = "\x1b[2;23m"
    BLACK = "\033[30m"

    # Special
    CRITICAL = "\x1b[30;41m"
    TIME = "\x1b[35;3m"

    BOLD = "\033[1m"
    NOBOLD = "\033[0m"

    # HREF
    HREF = "\x1b[2;23m"

    # Red shades
    RED_DARK = "\x1b[38;5;196m"
    RED_MEDIUM_DARK = "\x1b[38;5;202m"
    RED_MEDIUM = "\x1b[38;5;208m"
    RED_MEDIUM_LIGHT = "\x1b[38;5;214m"
    RED_LIGHT = "\x1b[38;5;220m"

    # Happy
    PINK = "\x1b[38;5;206m"
    PURPLE = "\x1b[38;5;141m"
    CYAN = "\x1b[38;5;87m"
    TEAL = "\x1b[38;5;37m"
    LILAC = "\x1b[38;5;183m"
    MINT = "\x1b[38;5;84m"

    # Pastel Colors
    PASTEL_PINK = "\x1b[38;5;218m"  
    PASTEL_PURPLE = "\x1b[38;5;183m"  
    PASTEL_BLUE = "\x1b[38;5;153m" 
    PASTEL_GREEN = "\x1b[38;5;120m" 
    PASTEL_YELLOW = "\x1b[38;5;226m"  
    PASTEL_ORANGE = "\x1b[38;5;223m"  
    PASTEL_CYAN = "\x1b[38;5;87m"  
    PASTEL_LILAC = "\x1b[38;5;183m"  
    PASTEL_MINT = "\x1b[38;5;121m"  

    # Background Colors
    BG_GRAY = "\x1b[48;5;238m" 
    BG_DARK_GRAY = "\x1b[48;5;236m" 
    BG_BLACK = "\x1b[48;5;232m" 
    BG_BLUE = "\x1b[48;5;27m" 
    BG_GREEN = "\x1b[48;5;28m"  
    BG_RED = "\x1b[48;5;52m" 
    BG_YELLOW = "\x1b[48;5;226m"  
    BG_ORANGE = "\x1b[48;5;202m"  
    BG_PURPLE = "\x1b[48;5;129m"  
    BG_PINK = "\x1b[48;5;206m"  
    BG_CYAN = "\x1b[48;5;45m"  
    BG_TEAL = "\x1b[48;5;30m"  


class Files:
    ROOT_DIR = Path(__file__).parent
    FILE1 = ROOT_DIR / "open.py"



"""
class ConfigDefaults:
    open_header = config['commands']['open']['header']
    open_pager = config['commands']['open']['pager']
    open_download = config['commands']['open']['download']
    open_log = config['commands']['open']['log']
    open_nodriver = config['commands']['open']['nodriver']
    open_parser = config['commands']['open']['parser']

    search_query = config['commands']['search']['query']
    search_header = config['commands']['search']['header']
    search_nodriver = config['commands']['search']['nodriver']
    search_log = config['commands']['search']['log']

    whois_header = config['commands']['whois']['header']

    find_element = config['commands']['find']['element']
    find_header = config['commands']['find']['header']
    find_log = config['commands']['find']['log']
    find_locator = config['commands']['find']['locator']

    quizlet_header = config['commands']['quizlet']['header']
    quizlet_pager = config['commands']['quizlet']['pager']
"""
