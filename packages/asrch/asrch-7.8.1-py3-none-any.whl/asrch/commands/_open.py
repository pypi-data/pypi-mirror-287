"""
open command
"""

import logging
import os
import random
import shutil
import sys
import time
import urllib
import urllib.request
from collections.abc import Generator
from datetime import datetime
from typing import Optional

import requests
from ascli.modules._box import Box
from ascli.modules._output import Output
from ascli.modules._alert import Alert
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import (
    ElementNotVisibleException,
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from asrch.modules._formatting import Bar
from asrch.modules.logging_formatter import ColorFormatter
from asrch.utils.constants import Colors

today = datetime.today().date()
#formatted_date = today.strftime("%m%d")  
form = Bar()
options = Options()
colors = Colors()
history: list[str] = []  # session history for browse mode
terminal_size = round(shutil.get_terminal_size().columns)

current_dir = os.path.dirname(os.path.realpath(__file__))
output_file_path = os.path.join(current_dir, "../../../workspaces/")
resolved_path = os.path.abspath(output_file_path)

c_log = logging.getLogger(__name__)
sh = logging.StreamHandler()

c_form = ColorFormatter("%(asctime)s|%(levelname)8s|%(message)s")

sh.setFormatter(c_form)

c_log.addHandler(sh)


def highlight_elements(soup):
    """
    Highlight all elements in BeautifulSoup object
    """
    for tag in soup.find_all(["h1"]):
        if tag.string is not None:
            tag.string = Box.create_box(None, tag.string, None, padding=2, style="h1")

    for tag in soup.find_all(["h2"]):
        if tag.string is not None:
            tag.string = Box.create_box(None, tag.string, None, padding=2, style="h2")

    for tag in soup.find_all(["h3", "p"]):
        if tag.string is not None:
            tag.string = Box.create_box(None, tag.string, None, padding=2, style="h3")

    for tag in soup.find_all("a", href=True):
        href = tag.get("href")
        if href:
            tag.string = f"{tag.string}({href})"
    return soup


def get_page(
    url: str | int,
    header: bool = False,
    proxy: Optional[str] = None,
    log=True,
    parser="html.parser",
    browse: bool = False,
) -> str | int:
    """Get the content of a web page.

    :param url: The URL of the web page.
    :type url: str
    :param header: Flag indicating whether to include headers in the request, defaults to False.
    :type header: bool, optional
    :param proxy: Proxy to be used for the request, defaults to None.
    :type proxy: Optional[str], optional
    :param log: Flag indicating whether to log actions, defaults to True.
    :type log: bool, optional
    :param parser: The parser to use for BeautifulSoup, defaults to 'lxml'.
    :type parser: str, optional
    :param browse: Flag indicating whether to enter browse mode, defaults to False.
    :type browse: bool, optional
    :raises ValueError: If the URL is empty.
    :raises Exception: If there are issues with the request.
    :return: The content of the web page if successful, otherwise an error code.
    :rtype: Union[str, int]
    """
    return_string: str = ""
    page_index: list[str] = []
    curr_url: int = 0
    indextbl = "INDEX"

    if not header:
        options.add_argument("--headless")
    else:
        pass
    if proxy is not None:
        pass
    if log:
        pass

    with webdriver.Firefox(options=options) as driver:
        try:
            driver.get(url)
            WebDriverWait(driver, 4)
            body = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "body"))
            )
            soup = BeautifulSoup(body.get_attribute("outerHTML"), parser)
            anchor_tags = driver.find_elements(By.TAG_NAME, "a")

            urls = [
                tag.get_attribute("href")
                for tag in anchor_tags
                if tag.get_attribute("href") is not None
                and "javascript:" not in tag.get_attribute("href")
            ]
        except StaleElementReferenceException:
            c_log.warning(
                """Could not find element.
                [This is probably not asrch but the website] [See docs for potential fixed]
                Continuing"""
            )
    highlight_elements(soup)

    text_content = soup.body.get_text(separator="\n")
    try:
        for url_ in urls:
            curr_url += 1
            page_index.append(f"({curr_url}){url_}")
    except UnboundLocalError:
        c_log.error("Could not find page")

    if browse:
        formatted_string = ""
        text_content = f"""

        {text_content.strip().replace("\n\n", "").replace("", "").replace("None", "")}
            """

        Output.print(
            Box.create_box(
                f"Results {curr_url}",
                f"""{text_content})  
        """,
                f"\nINDEX\n{page_index}\nINDEX",
                padding=1,
                style="main",
            )
        )
        Alert.alert(1, "Finished")

        prompt = (
            "\n[q]uit, [h]istory ([<] back in history 1) " "or Enter page number: "
        )
        while page_num := input(prompt):
            if page_num not in ["q", "<"] and "h" not in page_num:
                page_num = page_num

                try:
                    print(f"Navigating to {urls[int(page_num) - 1]}")

                    history.append(urls[int(page_num) - 1])

                    if len(history) >= 2:
                        prev_history = (
                            history[-2]
                            .replace("https://", "")
                            .replace("www.", "")[:17]
                        )
                    else:
                        prev_history = ""
                    history_formatted = ", ".join(
                        [f"({i + 1}) {elem}" for i, elem in enumerate(history)]
                    )
                    formatted_string += (
                        f"{Colors.PASTEL_PURPLE}{prev_history}... "
                        f"{Colors.PASTEL_PINK}[<----] {Colors.PASTEL_MINT}[---->] "
                        f"{Colors.PASTEL_CYAN}{urls[int(page_num) - 1]}\n"
                        f"{Colors.PASTEL_BLUE}[HISTORY]\n"
                        f"{Colors.PASTEL_ORANGE}{history_formatted}\n"
                        f"{form.bar('.', '', t_color='', bg_color='')}"
                    )

                    print(formatted_string)

                    Alert.alert(2, "Loading...")

                    return urls[int(page_num) - 1]

                except ValueError:
                    c_log.error("Must be an int")
                    continue
                except IndexError:
                    c_log.error("Choose a correct number")
                    continue
                except UnboundLocalError:
                    c_log.error("Error finding page")
                    continue

            elif page_num == "q":
                return "q"
            elif "h" in page_num:
                history_val = page_num.replace("h", "")
                history_val = history_val
                try:
                    print(history[history_val])
                    return history[history_val]
                except IndexError:
                    c_log.warning(
                        "Please use proper value. Could not find history element"
                    )
                    continue
            elif page_num == "<":
                print(f"{colors.BOLD} Navigating back in history {colors.NC}")
                history_one = len(history) - 1
                return history[history_one]
            else:
                c_log.warning("Please enter proper value")
                continue

    else:
        return_string =f"""
        {indextbl}
        {text_content.strip().replace("\n\n\n\n", "").replace("\t", "").replace("None", "")}
        {indextbl}
        """
    return return_string
            
def get_image(
    url: str | None,
    proxy: Optional[str],
    header: bool,
    download: Optional[bool] = False,
    workspace: Optional[str] = None,
) -> Generator[str, None, None]:
    """Get the image from a URL.

    :param url: The URL of the image. If None, returns an empty generator.
    :param proxy: Proxy to be used for the request, defaults to None.
    :param header: Flag indicating whether to include headers in the request.
    :param download: Flag indicating whether to download the image, defaults to False.
    :raises ValueError: If the URL is empty.
    :raises NoSuchelementexception: If the element can't be found.
    :raises ElementNotVisibleException: If the element isn't visible in the DOM.
    :raises StaleElementReferenceException: If the element can no longer be accessed.
    :return: A generator yielding the image content as strings.
    """

    c_log.debug(url)
    c_log.debug(proxy)
    c_log.debug(header)

    if header:  # pragma: no cover
        c_log.info("Headless false")
    else:
        c_log.info("Headless true")
        options.add_argument("--headless")

    if proxy is not None:  # pragma: no cover
        c_log.info("Proxy set")

    with webdriver.Firefox(options=options) as driver:
        driver.get(url)
        WebDriverWait(driver, 4)

        try:
            image_is_visible = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "img"))
            )
            print(image_is_visible.text)
            c_log.debug("Found elements: <img>")

            if image_is_visible and download is False:
                images = driver.find_elements(By.TAG_NAME, "img")

                for image in images:
                    yield image.get_attribute("src")

            if image_is_visible and download is True:  # pragma: no cover
                images = driver.find_elements(By.TAG_NAME, "img")
                fname = f"{url}"
                head, _, _ = fname.partition(".com")
                filename = head.replace("https://www.", "").replace("/", " ")

                new_folder = f"images_{filename}_{formatted_date}{random.randint(1000, 5000)}"

                try:
                    os.mkdir(f"{resolved_path}/{workspace}/downloads/{new_folder}")
                except FileNotFoundError:
                    c_log.error("Error, trying to fix...")
                    os.mkdir(f"{resolved_path}/{workspace}/downloads/")
                    os.mkdir(f"{resolved_path}/{workspace}/downloads/{new_folder}")

                c_log.debug(f"Created new folder . . . {new_folder}")

                WebDriverWait(driver, 2)

                for _, image in enumerate(images):
                    src = image.get_attribute("src")
                    if src:
                        last_slash_index = src.rfind("/")
                        file_name = src[last_slash_index + 1 :]
                        time.sleep(3)
                        urllib.request.urlretrieve(
                            src, f"{resolved_path}/{workspace}/downloads/{new_folder}/{file_name[:12]}"
                        )
                        yield f"{Colors.GREEN}downloaded:{Colors.NC} {src} \
Downloaded to downloads/{resolved_path}/{src}"

        except NoSuchElementException:  # pragma: no cover
            c_log.error(
                "NoSuchElementException: Could not find search bar. Possible solutions:\n \
                + Change IP (you have been detected)\nCheck Internet \
                (element did not load in time)"
            )
            c_log.debug("|-> Continuing")

        except ElementNotVisibleException:  # pragma: no cover
            c_log.error("ElementNotVisibleException: Element not visible in DOM. ")
            c_log.debug("|-> Continuing")

        except StaleElementReferenceException:  # pragma: no cover
            c_log.error(
                Box.h2box(
                    None,
                    "Stale Element Reference Exception: Element cannot currently be accessed.",
                    None,
                ),
            )
            c_log.debug("|-> Continuing")

def get_screenshot(
    url: str, proxy: Optional[str], header: bool = False, log=True
) -> None:  # pragma: no cover
    """Take a screenshot of a web page.

    :param url: The URL of the web page.
    :type url: str
    :param proxy: Proxy to be used for the request, defaults to None.
    :type proxy: str, optional
    :param header: Flag indicating whether to include headers in the request, defaults to False
    :type header: bool
    :param log: Flag indicating whether to log actions, defaults to True.
    :type log: bool
    """

    c_log.debug(url)
    c_log.debug(proxy)
    c_log.debug(header)
    c_log.debug(log)

    if log:
        c_log.setLevel(logging.WARNING)
    else:
        c_log.setLevel(logging.DEBUG)

    if header:  # pragma: no cover
        c_log.info("Headless false")
    else:
        c_log.info("Headless true")
        options.add_argument("--headless")

    if proxy is not None:  # pragma: no cover
        c_log.info("Proxy set")

    with webdriver.Firefox(options=options) as driver:
        ipaddr = requests.get("https://checkip.amazonaws.com/", timeout=10).text
        c_log.debug("[✗]setting header")
        headers: dict[str, str] = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) \
            Gecko/20100101 Firefox/84.0",
        }

        c_log.debug(f"[✗]UA: {headers}")
        c_log.debug(f"[✗]IP: {ipaddr}")

        c_log.debug("Opening Driver")
        c_log.debug(f"Screnshotting {url}")

        WebDriverWait(driver, 2)
        driver.get(url)

        WebDriverWait(driver, 3)
        c_log.info("Taking Screenshot")
        c_log.debug("[D]Taking Screenshot")

        driver.save_screenshot("Screenshots/Screenshot-img.png")
        c_log.info("Screenshot saved to 'Screenshots' folder")

        c_log.info("Screenshot saved to 'Screenshots' folder")

def get_html(url: str, proxy: Optional[str], header: bool = False, log=True) -> str:
    """Get the HTML source code of a web page.

    :param url: The URL of the web page.
    :type url: str
    :param proxy: Proxy to be used for the request, defaults to None.
    :type proxy: str, optional
    :param header: Flag indicating whether to include headers in the request, defaults to False
    :type header: bool
    :param log: Flag indicating whether to log actions, defaults to True.
    :type log: bool
    :return: The HTML source code of the web page.
    :rtype: str
    """

    c_log.debug(url)
    c_log.debug(proxy)
    c_log.debug(header)
    c_log.debug(log)

    if log:
        c_log.setLevel(logging.WARNING)
    else:
        c_log.setLevel(logging.DEBUG)

    if header:  # pragma: no cover
        c_log.info("Headless false")
    else:
        c_log.info("Headless true")
        options.add_argument("--headless")

    with webdriver.Firefox(options=options) as driver:
        driver.get(url)
        time.sleep(3)
        WebDriverWait(driver, 3)
        return driver.page_source

def get_js(
    url: str, proxy: Optional[str], header: bool = False, log=True
) -> Generator[str, None, None]:
    """Get the JavaScript content from a web page.

    :param url: The URL of the web page.
    :type url: str
    :param proxy: Proxy to be used for the request, defaults to None.
    :type proxy: str, optional
    :param header: Flag indicating whether to include headers in the request, defaults to Fals.
    :type header: bool
    :param log: Flag indicating whether to log actions, defaults to True.
    :type log: bool
    :return: A generator yielding the JavaScript content as strings.
    :rtype: Generator[str, None, None]
    """

    c_log.debug(url)
    c_log.debug(proxy)
    c_log.debug(header)
    c_log.debug(log)

    if log:
        c_log.setLevel(logging.WARNING)
    else:
        c_log.setLevel(logging.DEBUG)

    pages: list[str] = []

    if header:  # pragma: no cover
        c_log.info("Headless false")
    else:  # pragma: no cover
        c_log.info("Headless true")
        options.add_argument("--headless")

    with webdriver.Firefox(options=options) as driver:
        driver.get(url)
        time.sleep(2)
        page = driver.find_elements(By.TAG_NAME, "script")

        for js in page:
            pages.append(js.get_attribute("src"))

        for jsurl in pages:
            if "google" not in jsurl and jsurl != "":
                driver.get(jsurl)
                time.sleep(2)
                body = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.TAG_NAME, "body"))
                )
                bar = form.bar("$", f"{jsurl}", Colors.RED, Colors.GREEN)
                print(bar)
                yield f"\n{body.text}"


def inspect(url: str, proxy: Optional[str], header: bool = False, log=True, parser = "html.parser") -> str:
    """Get the HTML source code of a web page.

    :param url: The URL of the web page.
    :type url: str
    :param proxy: Proxy to be used for the request, defaults to None.
    :type proxy: str, optional
    :param header: Flag indicating whether to include headers in the request, defaults to False
    :type header: bool
    :param log: Flag indicating whether to log actions, defaults to True.
    :type log: bool
    :return: The HTML source code of the web page.
    :rtype: str
    """

    if not header:
        options.add_argument("--headless")
    else:
        pass
    if proxy is not None:
        pass
    if log:
        pass

    with webdriver.Firefox(options=options) as driver:
        try:
            driver.get(url)
            WebDriverWait(driver, 4)
            body = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "body"))
            )
            soup = BeautifulSoup(body.get_attribute("outerHTML"), parser)
            anchor_tags = driver.find_elements(By.TAG_NAME, "a")

            urls = [
                tag.get_attribute("href")
                for tag in anchor_tags
                if tag.get_attribute("href") is not None
                and "javascript:" not in tag.get_attribute("href")
            ]
        except StaleElementReferenceException:
            c_log.warning(
                """Could not find element.
                [This is probably not asrch but the website] [See docs for potential fixed]
                Continuing"""
            )
    highlight_elements(soup)

