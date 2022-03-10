"""Unit test functions for dictionary."""

__author__ = "730359525"

from dictionary import invert, favorite_color, count
import pytest


def test_empty_dict() -> None:
    """Returning an empty dict, adding nothing. Edge test."""
    original_dict: dict[str, str] = dict()
    assert invert(original_dict) == {}


def test_two_items() -> None:
    """Inverting a simple two item dict."""
    original_dict: dict[str, str] = {'a': 'b', 'c': 'd'}
    assert invert(original_dict) == {'b': 'a', 'd': 'c'}


def test_error_message() -> None:
    """Testing for a KeyError response if duplicated values are turned into duplicate keys."""
    with pytest.raises(KeyError):
        my_dictionary: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_counting_nothing() -> None:
    """Returning no list, when empty list is provided."""
    test: list[str] = []
    assert count(test) == []


def test_counting_multiple_of_3() -> None:
    """Counting to 3 when there is a value repeated thrice."""
    ex: list[str] = ["value", "value", "value"]
    assert count(ex) == {'value': 3}


def test_counting_rept_and_non_rept() -> None:
    """Counting both repeating and non-repeating key items."""
    ex: list[str] = ["value", "value", "value", "abnormal", "unusual"]
    assert count(ex) == {'value': 3, 'abnormal': 1, 'unusual': 1}


def test_favorite_color_blue() -> None:
    """Given a dict of data with blue being the most common, blue will be returned."""
    ex: dict[str, str] = {'Carl': 'Blue', 'Sam': 'Red', 'Ben': 'Blue', 'Steve': 'Green'}
    assert favorite_color(ex) == 'Blue'


def test_favorite_color_first() -> None:
    """Given a dict with no common color, the first color entered will be returned."""
    ex: dict[str, str] = {'Carl': 'Blue', 'Sam': 'Red', 'Ben': 'Yellow', 'Steve': 'Green'}
    assert favorite_color(ex) == 'Blue'


def test_fav_color_absent() -> None:
    """Given a dict with no content, nothing will be returned."""
    ex: dict[str, str] = {}
    assert favorite_color(ex) == {}