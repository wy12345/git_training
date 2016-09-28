from calc import add
from calc import pow

def test_add():
    assert add(1, 2) == 3

def test_pow():
    assert pow(1,2) == 1
    assert pow(2,2) == 4
    assert pow(10,0) == 1