import pytest
from demo.fib import fib


@pytest.mark.parametrize(("n", "expected"), [
    (1, 0),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 3),
    (6, 5),
    (7, 8),
    (8, 13),
    (9, 21),
    (10, 34)
])
def test_fib(n, expected):
    assert fib(n) == expected
