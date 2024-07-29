"""
open command
"""

import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from asrch.modules._formatting import Bar
from asrch.modules.logging_formatter import ColorFormatter



form = Bar()
options = Options()

c_log = logging.getLogger(__name__)
c_log.setLevel(logging.DEBUG)

sh = logging.StreamHandler()

c_form = ColorFormatter("%(asctime)s|%(levelname)8s|%(message)s")

sh.setFormatter(c_form)

c_log.addHandler(sh)


def get_quizlet(self, url: str, proxy: str, header: bool):
    """Gets the content of the <body> tag from a specified URL.

    :param url: The URL from which to fetch the <body> content.
    :type url: str
    :param proxy: The proxy server address to use for the request.
    :type proxy: str
    :param header: Whether to include custom headers in the request.
    :type header: bool
    :return: A list of strings containing the <body> content.
    :rtype: list
    """

    c_log.debug(self.url)
    c_log.debug(self.proxy)
    c_log.debug(self.header)

    if header:
        c_log.info("Headless false")
    else:
        c_log.info("Headless true")
        options.add_argument("--headless")

    if proxy is not None:
        c_log.info("Proxy set")
    elif proxy is None:
        c_log.debug("no proxy set")

    with webdriver.Firefox(options=options) as driver:
        output: list[str] = []
        c_log.info("Getting quizlet set")
        driver.get(url)
        time.sleep(3)
        WebDriverWait(driver, 4)
        body = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "body"))
        )

        output.append(body.text)
        return "\n".join(output)
