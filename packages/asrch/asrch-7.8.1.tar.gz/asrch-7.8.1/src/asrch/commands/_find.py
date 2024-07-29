"""
Find and return specified element with given URL
"""

import logging
from typing import Optional

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from asrch.modules._formatting import Bar
from asrch.modules.logging_formatter import ColorFormatter

options = Options()


c_log = logging.getLogger(__name__)

sh = logging.StreamHandler()

c_form = ColorFormatter("%(asctime)s|%(levelname)8s|%(message)s")

sh.setFormatter(c_form)

c_log.addHandler(sh)



def find_elements(
    url: str,
    locator: str,
    element: str,
    header: bool = False,
    proxy: Optional[str] = None,
    log=True,
) -> str:
    """
    Find elements based on given locator + element name
    The possible locators are: TAG_NAME, CLASS_NAME, ID, XPATH


    :param url: The URL of the web page.
    :type url: str
    :param element: The element to return
    :type element: str
    :param proxy: Proxy to be used for the request, defaults to None.
    :type proxy: Optional[str], optional
    :param header: Flag indicating whether to include headers in the request, defaults to False.
    :type header: bool, optional
    :raises ValueError: If the URL is empty.
    :raises Exception: If there are issues with the request.
    :return: The content of the web page.
    :rtype: str
    """

    c_log.debug(url)
    c_log.debug(element)
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
        output: str = ""
        c_log.info(f"Looking for element {element}")
        driver.get(url)
        try:
            if locator.lower() in ["tag", "tag_name"]:  # TAG NAME
                body = WebDriverWait(driver, 10).until(
                    EC.visibility_of_all_elements_located((By.TAG_NAME, element))
                )
            if locator.lower() in ["class", "class_name"]:  # CLASS NAME
                body = WebDriverWait(driver, 10).until(
                    EC.visibility_of_all_elements_located((By.CLASS_NAME, element))
                )
            if locator.lower() in ["id"]:  # ID
                body = WebDriverWait(driver, 10).until(
                    EC.visibility_of_all_elements_located((By.ID, element))
                )
            if locator.lower() in ["xpath", "x"]:  # XPATH
                body = WebDriverWait(driver, 10).until(
                    EC.visibility_of_all_elements_located((By.XPATH, element))
                )
            else:
                c_log.error("No valid locator used...")

        except NoSuchElementException:
            c_log.error(f"Could not find {element}")
        except TimeoutException:
            c_log.error(f"Timed out. Could not find {element} in 10s")
        try:
            for elem in body:
                output += Bar.bar("-", "Element", "", "") + "\n"
                output += str(elem) + "\n"
                output += Bar.bar("-", "Element", "", "") + "\n"
                output += elem.text + "\n"
        except UnboundLocalError:
            c_log.error(f"Please try again {locator.lower()}")
        return output
