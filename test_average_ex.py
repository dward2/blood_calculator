import pytest


@pytest.mark.parametrize("list_to_ave, expected", [
    ([1, 2, 3], 2),
    ([-2, -1, 0, 1, 2], 0),
    ([3], 3)
    ])
def test_my_average(list_to_ave, expected):
    from average_ex import my_average
    answer = my_average(list_to_ave)
    assert answer == expected
