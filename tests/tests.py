def power(x, y):
    return x**y


def increment(x):
    return x + 1


def decrement(x):
    return x - 1


def compare_length(x, y):
    return len(x) == len(y)


def test_increment():
    assert increment(4) == 5


def test_decrement():
    assert decrement(4) == 3


def test_power():
    assert power(2, 3) == 8


def test_compare_length():
    assert compare_length("1234", "abcd") == True
