import pytest
from project.model.nurl import NUrl


def test_properties_are_set():
    nurl = NUrl(short_url="short", original_url="original")
    assert nurl.short_url == "short"
    assert nurl.original_url == "original"
