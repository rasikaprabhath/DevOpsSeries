# test_calculator.py

from calculator_jenkins import add, subtract, multiply, divide

def test_add():
    assert add(3, 5) == 8

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 3) == 9

def test_divide():
    assert divide(10, 2) == 5
