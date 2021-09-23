import pytest
import mock
from project.lib.url_shortener import UrlShortener


def firstint(low, high):
    return 97


def lastint(low, high):
    return 122


def test_chars_are_predictable():
    with mock.patch('random.randint', firstint):
        shortened = UrlShortener.shorten_url()
        assert next(shortened) == "{url}a".format(url=UrlShortener.base_url)
        assert next(shortened) == "{url}b".format(url=UrlShortener.base_url)
        assert next(shortened) == "{url}c".format(url=UrlShortener.base_url)


def test_multiple_chars_are_predictable():
    with mock.patch('random.randint', lastint):
        times = 0
        for shortened in UrlShortener.shorten_url():
            times = times + 1
            if times >= 2:
                break

        assert shortened == "{url}zz".format(url=UrlShortener.base_url)
