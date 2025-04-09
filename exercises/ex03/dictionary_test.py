"A File to test the functions from dictionary"

import pytest
from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


__author__: str = "730549027"


# edge case
def test_invert_edge():
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


# use case
def test_invert_0():
    my_dictionary = invert({"a": "z", "b": "y", "c": "x"})
    assert my_dictionary == ({"z": "a", "y": "b", "x": "c"})


# use case
def test_invert_use_1() -> None:
    my_dictionary = invert({"apple": "banana"})
    assert my_dictionary == ({"banana": "apple"})


# edge case
def test_counts():
    my_dictionary = count([])
    assert my_dictionary == {}


# use Case
def test_counts_1():
    my_dictionary = count(["apple", "orange", "banana", "apple", "orange"])
    assert my_dictionary == ({"apple": 2, "orange": 2, "banana": 1})


# use case
def test_counts2():
    my_dictionary = count(["carrot", "leek", "carrot", "raddish"])
    assert my_dictionary == ({"carrot": 2, "leek": 1, "raddish": 1})


# edge case
def test_favorite_color_edge_cases():
    with pytest.raises(KeyError):
        assert favorite_color({}) == {}


# use case
def test_favorite_color():
    my_dictionary = favorite_color({"alice": "red", "bob": "green", "tim": "red"})
    assert my_dictionary == "red"


# use case
def test_favorite_color_1():
    my_dictionary = favorite_color(
        {"john": "blue", "jerry": "blue", "samantha": "blue"}
    )
    assert my_dictionary == "blue"


# edge case
def test_bins():
    with pytest.raises(KeyError):
        assert bin_len([]) == {}


# use case
def test_bins_1():
    my_dictionary = bin_len(["the", "quick", "fox"])
    assert my_dictionary == {3: {"the", "fox"}, 5: {"quick"}}


# use case
def test_bins_2():
    my_dictionary = bin_len(["the", "the", "fox"])
    assert my_dictionary == {3: {"the", "fox"}}
