from calc import add
from calc import pow

def test_add():
    assert add(1, 2) == 3

def test_pow():
    assert pow(1,2) == 1
    assert pow(2,2) == 4
    assert pow(10,0) == 1
    assert pow(0.5,2) == 0.25 
    assert pow(4,0.5) == 2

def test_mod():
	assert mod(5,2) == 1
