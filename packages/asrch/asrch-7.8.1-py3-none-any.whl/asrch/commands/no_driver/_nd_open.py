"""
A module providing the 'open' command as an alternative to the Selenium based command.
This command utilizes the requests library for HTTP requests and BeautifulSoup for HTML parsing.
"""

from pathlib import Path
import os
import re
import logging
from typing import Optional, Literal
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup, FeatureNotFound, Tag
import jsbeautifier

from asrch.modules.logging_formatter import ColorFormatter
from ascli.modules._alert import Alert
from ascli.modules._box import Box
from ascli.modules._output import Output
from ascli.modules._split import print_split_terminal
from ascli.utils.constants import Colors
from asrch.modules._formatting import Bar
from ascli.modules._highlighter import clean_and_format_urls as cln

history: list[str] = []  # session history for browse mode
tab_his:  list[str] = []
tabs_string: str = ""
tabs: list[str] = [] # tabs for browse mode sessions 
form = Bar()
colors = Colors()
c_log = logging.getLogger(__name__)
sh = logging.StreamHandler()

c_form = ColorFormatter("%(asctime)s|%(levelname)8s|%(message)s")

sh.setFormatter(c_form)

c_log.addHandler(sh)
config_path = Path(__file__).parent.parent.parent.parent.parent
path_with_config = config_path / '.config'

commands: list[str] = ["q", "<", "nt", "new_tab", "t", "sh", "show_history"]

def highlight_elements(soup: BeautifulSoup) -> BeautifulSoup:
    """
    Highlight all elements in BeautifulSoup object

    :param soup: The soup object to parse.
    :type: BeautifulSoup
    :return: soup
    :rtype: BeautifulSoup
    """

    for tag in soup.find_all(True):  
        if tag.string is not None and tag.name in ['div', 'hr']:
            tag.string = Box.create_box(None, tag.string, None, padding=1, style="h1u")

            separator_line = soup.new_tag('div')
            separator_line.string = "------------------------------------------------"
            try:
                tag.insert_before(separator_line)
                tag.insert_after(separator_line)
            except ValueError:
                continue
            
    for tag in soup.find_all("a"):
        if "href" in tag.attrs and tag["href"] is not None:
            tag["href"] = " * " + tag["href"]
        else:
            tag["href"] = " * "
    return soup

def get_index(url: str, mode: str = "") -> list[str]:
    """Fetches and processes URLs from a web page.

    :param url: The URL of the web page to fetch and process.
    :type url: str
    :param mode: Optional mode to determine the format of the output list. If `"url_list"`,
                 returns a list of URLs. Otherwise, returns a list with indexed URLs.
    :type mode: str, default is `""`
    :return: A list of URLs, either in indexed format or as a plain list depending on the mode.
    :rtype: list[str]
    :raises ValueError: If the provided URL is empty.
    :raises requests.exceptions.RequestException: If there is an error with the HTTP request.
    :raises FeatureNotFound: If BeautifulSoup cannot parse the HTML content.
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    proxies = {} 

    if not url:
        raise ValueError("URL cannot be empty")

    try:
        response = requests.get(url, proxies=proxies, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:

        print(f"Error occurred while fetching {url}: {str(e)}")
        return []

    try:
        soup = BeautifulSoup(response.content, "html.parser")
    except FeatureNotFound:
        return []

    href_list = []
    anchor_tags = soup.find_all("a")
    for anchor_tag in anchor_tags:
        if isinstance(anchor_tag, Tag):
            href = anchor_tag.get("href")
            if href:
                href_list.append(href)
                highlighted_content = anchor_tag.string
                if anchor_tag.string:
                    anchor_tag.string.replace_with(href)

    base_url = url
    url_list = []

    for url_ in href_list:
        modified_url = url_.replace("*", "").strip()  # Remove '*' and strip whitespace
        if modified_url.startswith("http"):
            url_list.append(modified_url)
        elif modified_url.startswith("/"):
            full_url = urljoin(base_url, modified_url)
            url_list.append(full_url)

    page_index = []
    try:
        for idx, url_ in enumerate(url_list, start=1):
            page_index.append(f"({idx}){url_}")
    except UnboundLocalError:
        print("Could not find page")
        
    if mode == "url_list": # this is absolutely fucking disgusting lets all ignore it :)
        return url_list
    else:
        return page_index

def handle_page_navigation_input(prompt: str, url_list: list[str], history: list[str], tabs: list[str], config_path: str) -> str:
    while True:
        page_num = input(prompt)
        try:
            if page_num not in commands and "h" not in page_num and "t" not in page_num:
                print(Colors.NC)
                try:
                    index = int(page_num) - 1
                    if 0 <= index < len(url_list):
                        print(f"Navigating to {url_list[index]}")
                        history.append(url_list[index])

                        prev_history = history[-2].replace("https://", "").replace("www.", "")[:17] if len(history) >= 2 else ""
                        history_formatted = ", ".join(f"({i + 1}) {elem}" for i, elem in enumerate(history))
                        formatted_string = f"{Colors.PASTEL_PURPLE}{prev_history}... {Colors.PASTEL_PINK}[<----] {Colors.PASTEL_MINT}[---->] {Colors.PASTEL_CYAN}{url_list[index]}\n{form.bar('.', '', t_color='', bg_color='')}"
                        
                        print(Colors.NC)
                        #print_split_terminal(left_text=f"* TABS\n{tabs_string}", right_text=f"* HISTORY\n{history}")
                        print(formatted_string)

                        Alert.alert(2, "Loading...")
                        return url_list[index]
                    else:
                        c_log.error(f"{index} Choose a correct number")
                except ValueError:
                    c_log.error("Must be an int")
                except IndexError as e:
                    print(e)
                    c_log.error("{page_num} Choose a correct number")
                except UnboundLocalError as e:
                    print(e)
                    c_log.error("Error finding page")
                except TypeError:
                    c_log.error("Bad input (maybe you put a url instead of int value?)")
            elif page_num == "q":
                print(Colors.NC)
                return "q"
            elif page_num.startswith("h"):
                try:
                    history_val = int(page_num[1:])
                    print(history[history_val])
                    return history[history_val]
                except IndexError:
                    c_log.warning("Please use proper value. Could not find history element")
            elif page_num in ["sh", "show_history"]:
                print(history)
            elif page_num == "<":
                try:
                    return history[-1]
                except IndexError:
                    c_log.warning("Please use proper value. Could not find history element")
            elif page_num in ["nt", "new_tab"]:
                get_url = input("url: ")
                tabs.append(get_url)
                tab_his.append(get_url)
                sub_index = []

                tabs_string = '\n'.join(f"{index + 1}. {tab}" for index, tab in enumerate(tabs))
                htab_string = '\n'.join(tab_his)
                tab_name = get_url.replace("https://", "")
                print(Colors.NC)
                print_split_terminal(left_text=f"* TABS\n{tabs_string}", right_text=f"* HISTORY\n{htab_string}")
                cfile_path = os.path.join(config_path, '.cache', f'{tab_name}.txt')
                if not os.path.exists(cfile_path):
                    try:
                        print(f"The file {cfile_path} does not exist in cache.")
                        with open(cfile_path, 'w') as f:
                            f.write(Box.create_box(
                                f"Results",
                                f"""{get_page(get_url)}""",
                                f"\n{get_index(get_url)}",
                                padding=1,
                                style="main",
                            ))
                        return get_url
                    except FileNotFoundError:
                        print(f"The file {cfile_path} does not exist in cache.")
                        return get_url
                else:
                   
                    search_string = "9b74c9897bac770ffc029102a200c5de7b5c6b4e715d0ab929c4a1c1f9f2b22d9eec09289c52ed0b2b38b4f3c7d5e2bd5d2a7cb63b223ce550501edbe2202"

                    with open(cfile_path, "r") as f:
                        found = False
                        for line in f:
                            if found:
                                # Clean the line and extract URLs
                                clean_line = line.replace(' ┋', '').replace('▢', '').replace('┉', '').strip()
                                urls = re.findall(r'https?://[^\s]+', clean_line)
                                sub_index.extend(urls)
                            elif search_string in line:
                                found = True

                    numbered_urls = [f"({idx}) {url}" for idx, url in enumerate(sub_index, start=1)]
                    Output.print(" ".join(numbered_urls))
                    page_num = 1

                    val = input(prompt)
                    if val == "nt":
                        get_url = input("Url: ")
                        result = get_url
                        return result
                    
                    try:
                        print(sub_index)

                        print(f"The URL at position {val} is: {result}")
                    except Exception as e:
                        print(e)
                        
                    print("return", result)
                    #return(result)   
            elif "t" in page_num and len(tabs) >= 1:
                try:
                    tab_value = int(page_num[1:])
                    print(f"{tabs[tab_value]}.txt")
                except IndexError:
                    c_log.error("Tab does not exist")
            else:
                c_log.warning("Please enter proper value")
        except TypeError:
            c_log.error(f"\"{page_num}\" Bad input (maybe you put a url instead of int value?)")


def get_page(
    url: str,
    header: str = "",
    proxy: Optional[dict[str, str]] = None,
    log: bool = True,
    *,
    parser: Optional[str] = "html.parser",
    browse: bool = False,
) -> str:
    """Get the content of a web page.

    :param url: The URL of the web page.
    :type url: str
    :param proxy: Proxy to be used for the request, defaults to None.
    :type proxy: Optional[str], optional
    :param log: Flag indicating whether to log the request, defaults to True.
    :type log: bool, optional
    :raises ValueError: If the URL is empty.
    :raises Exception: If there are issues with the request.
    :return: The content of the web page.
    :rtype: str
    """

    if not url:
        raise ValueError("URL cannot be empty")

    headers = {"User-Agent": "Mozilla/5.0"} if header else {}

    try:
        response = requests.get(url, proxies=proxy, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        c_log.error(f"Error occurred while fetching {url}: {str(e)}")
        return ""

    try:
        soup = BeautifulSoup(response.content, parser)
        title_tags = soup.find_all("title")
        highlight_elements(soup)

        for title_tag in title_tags:
            if isinstance(title_tag, Tag):
                title_tag.string = title_tag.string

        page_index = get_index(url)
        url_list = get_index(url, "url_list")
        text_content = soup.text.strip().replace("\n\n\n", "").replace("", "")
        
        if not browse:
            return text_content
        else:
            formatted_string = ""
            text_content = f"""{text_content.replace("None", "")}"""
            Output.print(
                Box.create_box(
                    f"Results",
                    f"""{text_content}""",
                    f"\nINDEX\n{' '.join(page_index)}\nINDEX",
                    padding=1,
                    style="main",
                )
            )
            Alert.alert(1, "Finished")

            prompt = (
                f"\n{Colors.PASTEL_PINK}\n"
                f"[{Colors.MINT}{Colors.BOLD}q{Colors.NC}{Colors.PASTEL_PINK}]uit\n"
                f"[{Colors.MINT}{Colors.BOLD}h{Colors.NC}{Colors.PASTEL_PINK}]istory ([<] back in history 1)\n"
                f"[{Colors.MINT}{Colors.BOLD}nt{Colors.NC}{Colors.PASTEL_PINK}] create new tab\n"
                f"[{Colors.MINT}{Colors.BOLD}t{Colors.NC}{Colors.PASTEL_PINK}] go to nth tab\n"
                f"or Enter page number:"
            )
            
            return handle_page_navigation_input(prompt, url_list, history, tabs, config_path)
            
    except FeatureNotFound:
        c_log.error('Could not find LXML parser \n quickfix: "pip install lxml"')
        return ""

def get_html(
    url: str,
    header: str = "",
    proxy: Optional[dict[str, str]] = None,
    log: bool = True,
    *,
    parser: Optional[str] = "html.parser",
) -> BeautifulSoup:
    """Get the content of a web page.
    
    :param url: The URL of the web page.
    :type url: str
    :param proxy: Proxy to be used for the request, defaults to None.
    :type proxy: Optional[str], optional
    :param log: Flag indicating whether to log the request, defaults to True.
    :type log: bool, optional
    :raises ValueError: If the URL is empty.
    :raises Exception: If there are issues with the request.
    :return: The content of the web page.
    :rtype: str
    """
    if not url:
        raise ValueError("URL cannot be empty")

    headers = {"User-Agent": "Mozilla/5.0"} if header else {}

    try:
        response = requests.get(url, proxies=proxy, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error occurred while fetching {url}: {str(e)}")
    try:
        soup = BeautifulSoup(response.content, parser)
    except FeatureNotFound:
        c_log.error('Could not find LXML parser \n quickfix: "pip install lxml"')
    return soup

def get_js(url: str, header: str = "", proxy: Optional[dict[str, str]] = None, log: bool = True, *, parser: Optional[str] = "html.parser") -> list[str] | str:
    """Get JavaScript sources from a web page."""
    jsoptions = jsbeautifier.default_options()
    if not url:
        raise ValueError("URL cannot be empty")

    headers = {"User-Agent": "Mozilla/5.0"} if header else {}

    try:
        response = requests.get(url, proxies=proxy, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error occurred while fetching {url}: {str(e)}")

    try:
        soup = BeautifulSoup(response.content, parser)
    except FeatureNotFound:
        raise Exception('Could not find BeautifulSoup parser')

    script_tags = soup.find_all('script')

    js_sources: list[str]  = []
    for script in script_tags:
        src = script.get('src')
        if src:
            # Convert relative URLs to absolute URLs
            full_url = urljoin(url, src)
            
            js_sources.append(full_url)

    output_source: list[str] = []
    for js_source in js_sources:
        try:
            output_source.append(get_page(js_source))
        except ValueError as e:
            print("===========================================")
            c_log.error(e)
            print("===========================================")
        except KeyError as e:
            print("===========================================")
            c_log.error(e)
            print("===========================================")
            continue
    return output_source 

def inspect(
    url: str,
    header: str = "",
    proxy: Optional[dict[str, str]] = None,
    log: bool = True,
    *,
    parser: Optional[str] = "html.parser",
    browse: bool = False,
    mode: Literal["js", "html"] = "html",
) -> None:
    """
    Inspects a web page by making an HTTP request with optional custom headers and proxies.

    :param url: The URL of the web page to inspect.
    :type url: str
    :param header: Optional custom headers to include in the HTTP request.
    :type header: str, default is `''`
    :param proxy: Optional dictionary of proxy settings to use for the HTTP request. If `None`, no proxies are used.
    :type proxy: dict[str, str] | None, default is `None`
    :param log: Whether to enable logging of the HTTP request and response. Default is `True`.
    :type log: bool, default is `True`
    :param parser: Optional HTML parser to use with BeautifulSoup. Default is `'html.parser'`. If `None`, no parser is specified.
    :type parser: str | None, default is `'html.parser'`
    :param browse: Whether to enable browsing mode, which might affect how the page content is processed. Default is `False`.
    :type browse: bool, default is `False`
    :param mode: Specifies the mode of operation. Can be either `'js'` for JavaScript processing or `'html'` for HTML parsing.
    :type mode: Literal['js', 'html'], default is `'html'`
    
    :return: This function does not return a value. It performs actions based on the provided parameters.
    :rtype: None

    :raises ValueError: If the `url` is empty or invalid.
    :raises requests.exceptions.RequestException: If there is an issue with the HTTP request.
    :raises FeatureNotFound: If the specified parser is not found or cannot parse the content.
    :raises Exception: For other unexpected errors that may occur during the inspection process.

    :note: 
        - Ensure that the `header` parameter is properly formatted as a valid header string.
        - The `proxy` dictionary should be formatted with valid proxy settings.
        - The `mode` parameter determines whether JavaScript or HTML parsing is used.
        - The `browse` parameter might affect how the content is handled, depending on its implementation.

    :seealso:
        - `BeautifulSoup` documentation for parsing options: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
        - `requests` documentation for HTTP request details: https://docs.python-requests.org/en/latest/
    """
    if not url:
        raise ValueError("URL cannot be empty")

    try:
        page_content = get_page(
            url=url, header=header, proxy=proxy, log=log, parser=parser
        )
        if mode == "html":
            inspect_content = get_html(
                url=url, header=header, proxy=proxy, log=log, parser=parser
            )

        if mode == "js":
            inspect_content = get_js(
                url=url, header=header, proxy=proxy, log=log, parser=parser
            )
        print_split_terminal(left_text=page_content, right_text=str(inspect_content))

    except ValueError as e:
        print(f"Error occurred during inspection: {str(e)}")

    return None
