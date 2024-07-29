import toml


def highlight_word(word, text, color_code):
    return text.replace(word, f"\x1b[{color_code}m{word}\x1b[0m")


config = toml.load("undetected.toml")

# Basic section
url = config["basic"]["url"]

# Privacy section
proxy = config["privacy"]["proxy"]

# Commands settings
open_header = config["commands"]["open"]["header"]
open_pager = config["commands"]["open"]["pager"]
open_download = config["commands"]["open"]["download"]
open_log = config["commands"]["open"]["log"]
open_nodriver = config["commands"]["open"]["nodriver"]
open_parser = config["commands"]["open"]["parser"]

search_query = config["commands"]["search"]["query"]
search_header = config["commands"]["search"]["header"]
search_nodriver = config["commands"]["search"]["nodriver"]
search_log = config["commands"]["search"]["log"]

whois_header = config["commands"]["whois"]["header"]

find_element = config["commands"]["find"]["element"]
find_header = config["commands"]["find"]["header"]
find_log = config["commands"]["find"]["log"]
find_locator = config["commands"]["find"]["locator"]

quizlet_header = config["commands"]["quizlet"]["header"]
quizlet_pager = config["commands"]["quizlet"]["pager"]


settings_list: list = []
# Basic section
settings_list.append(("url", config["basic"]["url"]))

# Privacy section
settings_list.append(("proxy", config["privacy"]["proxy"]))

# Commands settings
settings_list.append(search_query)

print(search_query)

highlighted_settings_list = []
"""for variable, value in settings_list:
    if "open" in variable:
        variable = highlight_word("open", variable, "1;33")  
    elif "search" in variable:
        variable = highlight_word("search", variable, "1;34") 
    elif "whois" in variable:
        variable = highlight_word("whois", variable, "1;35")  
    elif "find" in variable:
        variable = highlight_word("find", variable, "1;36")  
    elif "quizlet" in variable:
        variable = highlight_word("quizlet", variable, "1;31") 
    highlighted_settings_list.append((variable, value))"""

