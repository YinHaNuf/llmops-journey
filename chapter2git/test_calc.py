def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5     # 通过
    assert add(-1, 1) == 0      # 通过
    assert add(0, 0) == 0       # 通过 """

import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("不能除以零")
    return a / b

def test_divide_ok():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0) 


@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15

def test_len(sample_data):
    assert len(sample_data) == 5