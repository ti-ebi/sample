"""Tests for utility functions."""

import sys
from pathlib import Path

# Add src to path so we can import the module
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from sample.utils import greet, add_numbers, multiply_numbers, factorial


def test_greet():
    """Test the greet function."""
    assert greet("World") == "Hello, World!"
    assert greet("Python") == "Hello, Python!"
    assert greet("") == "Hello, !"


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    assert add_numbers(100, 200) == 300


def test_multiply_numbers():
    """Test the multiply_numbers function."""
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(0, 5) == 0
    assert multiply_numbers(-2, 3) == -6
    assert multiply_numbers(10, 10) == 100


def test_factorial():
    """Test the factorial function with valid inputs."""
    # Base cases
    assert factorial(0) == 1
    assert factorial(1) == 1

    # Small numbers
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120

    # Larger numbers
    assert factorial(10) == 3628800
    assert factorial(12) == 479001600


def test_factorial_negative():
    """Test that factorial raises ValueError for negative inputs."""
    import pytest
    with pytest.raises(ValueError, match="not defined for negative values"):
        factorial(-1)
    with pytest.raises(ValueError, match="not defined for negative values"):
        factorial(-10)


def test_factorial_non_integer():
    """Test that factorial raises TypeError for non-integer inputs."""
    import pytest
    with pytest.raises(TypeError, match="must be an integer"):
        factorial(3.5)
    with pytest.raises(TypeError, match="must be an integer"):
        factorial("5")
    with pytest.raises(TypeError, match="must be an integer"):
        factorial([5])
