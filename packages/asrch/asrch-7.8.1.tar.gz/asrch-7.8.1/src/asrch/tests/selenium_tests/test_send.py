"""
Tests for selenium commands._send
"""

from asrch.commands._send import search_engines


def test_sends() -> None:
    """
    Tests get image function
    """

    assert "https" in search_engines(query="test", proxy=None, header=False)
