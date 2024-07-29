"""
Send command
"""

import logging
import random
import time
from typing import Optional

from selenium import webdriver
from selenium.common.exceptions import (
    ElementNotVisibleException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from asrch.modules.logging_formatter import ColorFormatter
from asrch.utils.constants import Colors

options = Options()


c_log = logging.getLogger(__name__)

sh = logging.StreamHandler()

c_form = ColorFormatter("%(asctime)s|%(levelname)8s|%(message)s")

sh.setFormatter(c_form)

c_log.addHandler(sh)

# CONSTANTS
DDG_URL: str = "https://lite.duckduckgo.com/html"
GGL_URL: str = "https://www.google.com/search"

url_index: list[str] = []



def scroll_down(driver) -> None:
    """Scrolls page until the end is reached

    :param driver: the driver to execute the script on
    :type driver: object
    :returns: None
    """
    c_log.debug("Scrolling")
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        WebDriverWait(driver, random.randrange(0, 2))

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height

def search_ddg(
    query: str, header: bool, proxy: Optional[str], log: bool
) -> list[str]:
    """Opens Google and searches for a query given by the user.

    :param url: The URL passed from the click argument, defaults to None
    :raises ValueError: If the URL is not provided
    :raises NoSuchelementexception: If the element can't be found.
    :raises ElementNotVisibleException: If the element isn't visible in the DOM.
    :return: The list of URLs from the webpage
    :rtype: list[str]
    """
    output: list[str] = [""]
    
    if log:
        c_log.setLevel(logging.DEBUG)
    else:
        c_log.setLevel(logging.WARNING)


    if header:  # pragma: no cover
        c_log.info("Headless false")
    else:
        c_log.info(
            "Headless true"
        )  # why does true mean no header LOL (not fixing it)
        options.add_argument("--headless")

    if proxy is not None:  # pragma: no cover
        c_log.info("Proxy set")

    with webdriver.Firefox(options=options) as driver:
        try:
            c_log.debug("Opening Driver")
            c_log.debug(DDG_URL)
            driver.get(DDG_URL)

            c_log.debug("Loooking for search bar")
            text_area = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "search__input"))
            )

            WebDriverWait(driver, random.randrange(0, 2))
            text_area.send_keys(query)

            c_log.debug(f"Sending {query}")

            WebDriverWait(driver, random.randrange(0, 2))
            text_area.send_keys(Keys.ENTER)
            time.sleep(2) 

            lnks = driver.find_elements(By.XPATH, "//a[@href]")
            seen_urls = set()
            for lnk in lnks:
                _url = lnk.get_attribute("href")
                _title = lnk.get_attribute("text")
                
                
                if _url not in seen_urls:
                    seen_urls.add(_url)
                    url_index.append(_url)
                    output.append(
                        f"\033[1m {Colors.MINT}{_title.strip()}\033[0m\n{_url}\n"
                    )

            blacklist: list[str] = [
                "spreadprivacy",
                "javascript:",
                "bing",
                "bingj",
                "yahoo",
                "google",
                "duckduckgo",
            ]
            if not any(val in _url for val in blacklist):
                for urls in seen_urls:
                    seen_urls.add(urls)

        except NoSuchElementException as e:
            c_log.error(e)
            c_log.error("No element\n\t'-> continuing")

        except ElementNotVisibleException as e:
            c_log.error(e)
            c_log.error("Element not visible\n\t'-> continuing")

        except TimeoutException as e:
            c_log.error(e)
            c_log.error("Timed out\n\t'-> continuing")

        return output

def search_ggl(query: str, header: bool, proxy: Optional[str], log: bool) -> str:
    """Opens Google and searches for a query given by the user.

    :param url: The URL passed from the click argument, defaults to None
    :raises ValueError: If the URL is not provided
    :raises NoSuchelementexception: If the element can't be found.
    :raises ElementNotVisibleException: If the element isn't visible in the DOM.
    :raises Timeoutexception: If seleniumm times out waiting for element.
    :return: The list of URLs from the webpage
    :rtype: list[str]
    """
    output: list[str] = [""]

    if log:
        c_log.setLevel(logging.DEBUG)
    else:
        c_log.setLevel(logging.WARNING)

    if header:  # pragma: no cover
        c_log.info("Headless false")
    else:
        c_log.info(
            "Headless true"
        )  # why does true mean no header LOL (not fixing it)
        options.add_argument("--headless")

    if proxy is not None:  # pragma: no cover
        c_log.info("Proxy set")

    with webdriver.Firefox(options=options) as driver:
        try:
            c_log.debug("Opening Driver")
            c_log.debug(GGL_URL)
            driver.get(GGL_URL)
            c_log.debug("Loooking for search bar")
            text_area = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "gLFyf"))
            )
            WebDriverWait(driver, 2)
            text_area.send_keys(query)

            c_log.debug(f"Sending {query}")

            WebDriverWait(driver, random.randrange(0, 2))
            text_area.send_keys(Keys.ENTER)
            time.sleep(3)  
            lnks = driver.find_elements(By.XPATH, "//a[@href]")
            curr_url = 0
            seen_urls = set()
            i = 0
            for lnk in lnks:
                _url = lnk.get_attribute("href")
                _title = lnk.get_attribute("text")  # Get the title attribute
                i += 1

                if _url not in seen_urls:
                    seen_urls.add(_url)
                    output.append(
                        f"\033[1m {Colors.MINT}{_title.strip()}\033[0m\n{_url}\n"
                    )

        except NoSuchElementException as e:
            c_log.error(e)
            c_log.error("No element\n\t'-> continuing")

        except ElementNotVisibleException as e:
            c_log.error(e)
            c_log.error("Element not visible\n\t'-> continuing")

        except TimeoutException as e:
            c_log.error(e)
            c_log.error("Timed out\n\t'-> continuing")

        return output


def search_engines(
        query: str, header: bool = False, proxy: Optional[str] = None, log: bool = True, browse = False
) -> str | int:
    output: list[str] = []

    ddg_links = search_ddg(query, header=header, proxy=proxy, log=log)
    output.extend(ddg_links)
    
    
    # Collect links from Google
    ggl_links = search_ggl(query, header=header, proxy=proxy, log=log)
    output.extend(ggl_links)

    if browse:
        for index, line in enumerate(output, start=1):
            print(f"{index}. {line}")
            
        prompt = (
            "\n[q]uit, [h]istory ([<] back in history 1) " "or Enter page number: "
        )
        
        while page_num := int(input(prompt)):
            if page_num not in ["q", "<"]:
                print(f"Navigating to {url_index[page_num - 2]}")
                formatted_string = (
                        f"{Colors.PASTEL_PINK}[<----] {Colors.PASTEL_MINT}[---->] "
                        f"{Colors.PASTEL_CYAN}{url_index[int(page_num) - 1]}\n"
                        f"{Colors.PASTEL_BLUE}[HISTORY]\n"
                    )

                print(formatted_string)
                return (url_index[page_num - 2])


    else:
        return "\n".join(output)
        
