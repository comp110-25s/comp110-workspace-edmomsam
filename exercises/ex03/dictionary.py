"4 Functions to Test Against"

__author__: str = "730549027"


def invert(di: dict[str, str]) -> dict[str, str]:
    "A function to invert the order of dictionaries"
    keys = list(di.keys())
    values = list(di.values())

    if len(set(values)) != len(values):
        raise KeyError("Repeat value, can not invert")

    inverted: dict[str, str] = {}
    idx: int = 0
    while idx < len(keys):
        inverted[values[idx]] = keys[idx]
        idx += 1
    return inverted


def count(counter: list[str]) -> dict[str, int]:
    "Counts the frequences of the values in a dictionary"
    result: dict[str, int] = {}
    idx: int = 0
    while idx < len(counter):
        item = counter[idx]
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
        idx += 1
    return result


def favorite_color(favorites: dict[str, str]) -> str:
    "Returns the most frequently occuring color in the dictionary"

    color_count = count(list(favorites.values()))
    max_count = 0
    fav = ""
    colors = list(favorites.values())
    idx = 0

    while idx < len(colors):
        color = colors[idx]
        if color_count[color] > max_count:
            max_count = color_count[color]
            fav = color

        idx += 1
    return fav


def bin_len(input: list[str]) -> dict[int, set[str]]:
    "Returns a dictionary of integers of length for an input"
    bins: dict[int, set[str]] = {}
    idx: int = 0
    while idx < len(input):
        word = input[idx]
        length = len(word)
        if length not in bins:
            bins[length] = set()
        bins[length].add(word)
        idx += 1
    return bins
