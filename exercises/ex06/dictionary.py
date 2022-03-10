"""Dictionaries for ex06."""

__author__ = "730359525"


def invert(original_dict: dict[str, str]) -> dict[str, str]:
    """Inverts key-value pairs of x."""
    flipped: dict[str, str] = {}
    for key in original_dict:
        if original_dict[key] in flipped:
            raise KeyError("Duplicate key value.")
        flipped[original_dict[key]] = key            
    return flipped


def count(xs: list[str]) -> dict[str, int]:
    """Numbering keys of a list to make a dict."""
    storage: dict[str, int] = dict()
    for x in xs:
        if x in storage:
            storage[x] += 1
        else:
            storage[x] = 1
    return storage


def favorite_color(xs: dict[str, str]) -> str:
    """Finding the most common value in a dict."""
    flipped = {}
    multiples: list[str] = []
    for x in xs:
        multiples.append(xs[x])
    flipped = count(multiples)
    favorite_color: str = ""
    i: int = 0
    for x in flipped:
        if flipped[x] > i:
            i = flipped[x]
            favorite_color = x
    return favorite_color