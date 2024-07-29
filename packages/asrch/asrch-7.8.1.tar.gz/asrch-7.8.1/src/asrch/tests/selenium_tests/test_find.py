"""
Tests for find command
"""

import pytest
from selenium import webdriver

from asrch.commands._find import find_elements




def test_id() -> None:
    """
    Tests id function
    """

    assert "Countries of the World" in (
        find_elements(
            "https://www.scrapethissite.com/pages/simple",
            "ID",
            "page",
            header=False,
            proxy=None,
        )
    )


def test_tag_name() -> None:
    """
    Tests tag_name function
    """

    assert "Scrape This Site" in (
        find_elements(
            "https://www.scrapethissite.com/pages/simple",
            "TAG_NAME",
            "a",
            header=False,
            proxy=None,
        )
    )


def test_class_name() -> None:
    """
    Tests class_name function
    """

    assert "Countries of the World" in (
        find_elements(
            "https://www.scrapethissite.com/pages/simple",
            "CLASS_NAME",
            "row",
            header=False,
            proxy=None,
        )
    )


def test_xpath() -> None:
    """
    Tests xpath function
    """

    assert "Countries of the World" in (
        find_elements(
            "https://www.scrapethissite.com/pages/simple",
            "XPATH",
            "/html/body/div/section/div/div[1]/div/h1",
            header=False,
            proxy=None,
        )
    )
