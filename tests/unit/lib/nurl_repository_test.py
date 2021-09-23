import pytest
from project.lib.nurl_repository import NUrlRepository


def test_repository_is_a_singleton():
    subject = NUrlRepository.get_instance()
    assert len(subject.shortened) == 0
    assert len(subject.originals) == 0
    assert subject is not None


def test_one_ring_to_rule_them_all():
    NUrlRepository.get_instance()
    with pytest.raises(Exception):
        NUrlRepository()


def test_nurl_is_created():
    subject = NUrlRepository.get_instance()
    subject.get_or_create("url")
    assert len(subject.shortened) == 1
    assert len(subject.originals) == 1


def test_nurl_is_not_duplicated():
    subject = NUrlRepository.get_instance()
    subject.get_or_create("url")
    subject.get_or_create("url")
    assert len(subject.shortened) == 1
    assert len(subject.originals) == 1


def test_original_url_is_retrieved():
    subject = NUrlRepository.get_instance()
    shorty = subject.get_or_create("url").short_url
    original = subject.get_by_shortened(shorty).original_url
    assert original == "url"
