import pytest
from src.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_addition(calc):
    assert calc.add(2, 3) == 5

def test_subtraction(calc):
    assert calc.subtract(5, 3) == 2

def test_division_error(calc):
    with pytest.raises(ValueError):
        calc.divide(5, 0)
