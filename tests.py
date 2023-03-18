import pytest
from main import summ


def test_summ_func():
    assert summ(17, -5) == 12

def test_summ_func_minus():
    assert summ(-1, -1) == -2


if __name__ == '__main__':
    pytest.main()
