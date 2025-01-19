import pytest
from app.rpn_calculator.calculator import RPNCalculator

@pytest.fixture
def calculator():
    return RPNCalculator()


# Test basic operations
def test_addition(calculator):
    result = calculator.calculate("3 4 +")
    assert result == 7


def test_subtraction(calculator):
    result = calculator.calculate("10 4 -")
    assert result == 6


def test_multiplication(calculator):
    result = calculator.calculate("3 4 *")
    assert result == 12


def test_division(calculator):
    result = calculator.calculate("8 4 /")
    assert result == 2


def test_division_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.calculate("3 0 /")


def test_square_root(calculator):
    result = calculator.calculate("9 sqrt")
    assert result == 3


def test_square_root_negative(calculator):
    with pytest.raises(ValueError):
        calculator.calculate("-9 sqrt")


def test_multiple_operations(calculator):
    result = calculator.calculate("3 4 + 5 *")
    assert result == 35


def test_missing_operation(calculator):
    with pytest.raises(ValueError):
        calculator.calculate("3 4")


def test_missing_operation_2(calculator):
    with pytest.raises(ValueError):
        calculator.calculate("3 4 5 +")


def test_missing_operand(calculator):
    with pytest.raises(ValueError):
        calculator.calculate("3 +")


def test_unknown_operator(calculator):
    with pytest.raises(ValueError):
        calculator.calculate("3 4 %")


def test_empty_expression(calculator):
    with pytest.raises(ValueError):
        calculator.calculate("")


def test_long_expression(calculator):
    result = calculator.calculate("3 4 + 2 * 7 / 4 4 + +")
    assert result == 10


def test_floating_point_result(calculator):
    result = calculator.calculate("3 4 + 2 * 5 /")
    assert result == 2.8


# Test single operand for square root
def test_operation_with_sqrt(calculator):
    result = calculator.calculate("5 5 * sqrt")
    assert result == 5


def test_invaid_expression(calculator):
    with pytest.raises(ValueError):
        calculator.calculate("a b +")

