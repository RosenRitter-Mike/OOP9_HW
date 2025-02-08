import pytest
from recursion import *

# # ______Ex. 1 test_________
print("=" * 9, " Ex.1 test", "=" * 9)
range_func(8, 15, 3)
range_func(10, 0, -1)
range_func(10, 2, 0)

# ______Ex. 2 test_________
def factorial_test_5():
    x: int = 5
    expected: int = 120

    # Act
    actual: int = factorial_func(x)

    # Assert
    assert actual == expected


def factorial_test_2():
    x: int = 2
    expected: int = 2

    # Act
    actual: int = factorial_func(x)

    # Assert
    assert actual == expected


def factorial_test_zero():
    x: int = 0
    expected: int = 1

    # Act
    actual: int = factorial_func(x)

    # Assert
    assert actual == expected


def factorial_test_neg():
    x: int = -3

    with pytest.raises(ValueError) as ex:
        actual: int = factorial_func(x)
        assert str(ex.value) == "MathError: the factorial of a negative number is not defined"


# ______Ex. 3 test_________
def digit_sum_test_86():
    x: int = 86
    expected: int = 14

    # Act
    actual: int = digit_sum_func(x)

    # Assert
    assert actual == expected


def digit_sum_test_404():
    x: int = 404
    expected: int = 8

    # Act
    actual: int = digit_sum_func(x)

    # Assert
    assert actual == expected


def digit_sum_test_zero():
    x: int = 0
    expected: int = 0

    # Act
    actual: int = digit_sum_func(x)

    # Assert
    assert actual == expected


def digit_sum_test_neg():
    x: int = -3456
    expected: int = -18

    # Act
    actual: int = digit_sum_func(x)

    # Assert
    assert actual == expected


# ______Ex. 4 test_________
def number_count_test():
    list_numbers: list = [1, -1, 2, -2, 0, -1, -2, -3, 1000, -2, 0]
    expected: int = list_numbers.count(-2)

    # Act
    actual: int = number_appearances_func(list_numbers, -2)

    # Assert
    assert actual == expected


factorial_test_5()
factorial_test_2()
factorial_test_zero()
factorial_test_neg()
print("=" * 9, " Ex.2 test passed", "=" * 9)
digit_sum_test_86()
digit_sum_test_404()
digit_sum_test_zero()
digit_sum_test_neg()
print("=" * 9, " Ex.3 test passed", "=" * 9)
number_count_test()
print("=" * 9, " Ex.4 test passed", "=" * 9)