# test_calculator.py - Hybrid PyTest demo (own code, adapted from docs.pytest.org/en/stable/how-to/assert.html, /how-to/fixtures.html, /how-to/parameterize.html, /how-to/mock.html)
import pytest
from unittest.mock import patch  # Built-in
from calculator import add, subtract, multiply, power, square_root, Calculator

# --- Fixture example ---


@pytest.fixture
def calc():
    """Fixture that provides a reusable Calculator instance."""
    return Calculator()

# --- Parametrized tests ---


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 4, 3),
    (0, 0, 0),
])
def test_add(a, b, expected):
    """Test add() using parametrization."""
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 4, 6),
    (-2, -3, 1),
    (5, -7, 12),
])
def test_subtract(a, b, expected):
    """Test subtract() using parametrization."""
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (0, 5, 0),
    (-1, -2, 2),
])
def test_multiply(a, b, expected):
    """Test multiply() using parametrization."""
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (9, 0.5, 3),
])
def test_power(a, b, expected):
    """Test power() function for positive and fractional exponents."""
    assert power(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("x, expected", [
    (4, 2),
    (9, 3),
    (0, 0),
])
def test_square_root(x, expected):
    """Test square_root() for valid inputs."""
    assert square_root(x) == pytest.approx(expected)


def test_square_root_negative():
    """Test square_root() for negative input - should raise ValueError."""
    with pytest.raises(ValueError, match="negative"):
        square_root(-9)

# --- Tests using the Calculator class and fixture ---


def test_divide(calc):
    """Test divide() using fixture instance."""
    assert calc.divide(10, 2) == 5


def test_divide_by_zero(calc):
    """Test divide() for division by zero."""
    with pytest.raises(ValueError, match="zero"):
        calc.divide(10, 0)


@pytest.mark.parametrize("numbers, expected", [
    ([2, 4, 6], 4),
    ([10, 20, 30, 40], 25),
])
def test_average(calc, numbers, expected):
    """Test average() for valid lists."""
    assert calc.average(numbers) == expected


def test_average_empty_list(calc):
    """Test average() for empty list - should raise ValueError."""
    with pytest.raises(ValueError):
        calc.average([])

# --- Mocking example (merged from V2) ---


@patch('calculator.math.sqrt')  # Key: Mocks module func
def test_mock_square_root(mock_sqrt):
    """Mock square_root to isolate math.sqrt dependency."""
    mock_sqrt.return_value = 3.0  # Force output
    result = square_root(9)  # Calls mocked sqrt(9)
    assert result == 3.0
    mock_sqrt.assert_called_once_with(9)  # Verify
