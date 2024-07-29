"""
Tests for no driver open command
"""

from unittest.mock import patch

import pytest
from bs4 import FeatureNotFound

from asrch.commands.no_driver._nd_open import ND_Open


@pytest.fixture
def mock_response():
    class MockResponse:
        def __init__(self, content, status_code):
            self.content = content
            self.status_code = status_code

        def raise_for_status(self):
            pass

    return MockResponse(b"<html><body><p>Hello World</p></body></html>", 200)


def test_get_page(mock_response):
    url = "https://www.scrapethissite.com/pages/simple/"

    with patch("requests.get") as mock_get:
        mock_get.return_value = mock_response
        page_content = ND_Open.get_page(url)

    assert page_content == "Hello World"


def test_get_html(mock_response):
    url = "https://example.com"

    with patch("requests.get") as mock_get:
        mock_get.return_value = mock_response
        soup = ND_Open.get_html(url)

    assert str(soup) == "<html><body><p>Hello World</p></body></html>"


def test_get_page_empty_url():
    with pytest.raises(ValueError):
        ND_Open.get_page("")


def test_get_html_empty_url():
    with pytest.raises(ValueError):
        ND_Open.get_html("")


def test_get_page_request_exception():
    with pytest.raises(Exception):
        ND_Open.get_page("")


def test_get_html_request_exception():
    with pytest.raises(Exception):
        ND_Open.get_html("")


def test_get_page_feature_not_found(mock_response):
    url = ""

    with patch("requests.get") as mock_get, patch("bs4.BeautifulSoup") as mock_bs:
        mock_get.return_value = mock_response
        mock_bs.side_effect = FeatureNotFound
        with pytest.raises(Exception):
            ND_Open.get_page(url)


def test_get_html_feature_not_found(mock_response):
    url = ""

    with patch("requests.get") as mock_get, patch("bs4.BeautifulSoup") as mock_bs:
        mock_get.return_value = mock_response
        mock_bs.side_effect = FeatureNotFound
        with pytest.raises(Exception):
            ND_Open.get_html(url)
