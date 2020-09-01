def test_add_1():
    from math_calculator import add
    answer = add(2, 3)
    expected = 5
    assert answer == expected


def test_add_2():
    from math_calculator import add
    answer = add(-1, 4)
    expected = 3
    assert answer == expected

