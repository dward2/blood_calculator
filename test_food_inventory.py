import pytest


@pytest.mark.parametrize("fruit, expected", [
    ("apple", True),
    ("pear", True),
    ("banana", True),
    ("peach", True),
    ("beef", False),
    ("Apple", True),
    (" apple ", True),
    ("aple", False),
    ("apples", True),
    ])
def test_is_fruit(fruit, expected):
    from food_inventory import is_fruit
    answer = is_fruit(fruit)
    assert answer == expected
