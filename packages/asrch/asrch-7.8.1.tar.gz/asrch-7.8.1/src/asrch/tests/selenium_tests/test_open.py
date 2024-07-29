"""
Tests for selenium commands._open
"""

from asrch.commands._open import get_page, get_html, get_image, get_js




def test_images():
    """
    Tests get image function
    """

    assert (
        "https://www.scrapethissite.com/static/images/scraper-icon.png"
        in get_image(
            "https://www.scrapethissite.com/pages/simple/", proxy=None, header=False
        )
    )


def test_text():
    """
    Tests get page funtion
    """

    assert "Countries of the World" in get_page(
        "https://www.scrapethissite.com/pages/simple/", proxy=None, header=False
    )


def test_html():
    """
    Tests HTML function
    """
    assert "<body>" in get_html(
        "https://www.scrapethissite.com/pages/simple/", proxy=None, header=False
    )


def test_js():
    """
    Tests javascript function
    """
    gen_iter = get_js(
        "https://www.scrapethissite.com/pages/simple/", proxy=None, header=False
    )
    try:
        next(gen_iter)
        assert "* Copyright" in next(gen_iter)
    except StopIteration:
        pass
