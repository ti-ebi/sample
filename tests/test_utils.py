"""Tests for utility functions."""

import sys
from pathlib import Path

# Add src to path so we can import the module
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from sample.utils import greet, add_numbers, multiply_numbers, factorial, is_prime


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


def test_is_prime_small_primes():
    """Test is_prime with small prime numbers."""
    # First few prime numbers
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(11) is True
    assert is_prime(13) is True
    assert is_prime(17) is True
    assert is_prime(19) is True
    assert is_prime(23) is True
    assert is_prime(29) is True


def test_is_prime_composite_numbers():
    """Test is_prime with composite numbers."""
    assert is_prime(4) is False
    assert is_prime(6) is False
    assert is_prime(8) is False
    assert is_prime(9) is False
    assert is_prime(10) is False
    assert is_prime(12) is False
    assert is_prime(15) is False
    assert is_prime(20) is False
    assert is_prime(100) is False


def test_is_prime_edge_cases():
    """Test is_prime with edge cases."""
    # 0 and 1 are not prime
    assert is_prime(0) is False
    assert is_prime(1) is False

    # Negative numbers are not prime
    assert is_prime(-1) is False
    assert is_prime(-5) is False
    assert is_prime(-10) is False


def test_is_prime_large_primes():
    """Test is_prime with larger prime numbers."""
    assert is_prime(97) is True
    assert is_prime(101) is True
    assert is_prime(199) is True
    assert is_prime(541) is True


def test_is_prime_large_composites():
    """Test is_prime with larger composite numbers."""
    assert is_prime(98) is False
    assert is_prime(100) is False
    assert is_prime(200) is False
    assert is_prime(540) is False


def test_is_prime_non_integer():
    """Test that is_prime raises TypeError for non-integer inputs."""
    import pytest
    with pytest.raises(TypeError, match="must be an integer"):
        is_prime(3.5)
    with pytest.raises(TypeError, match="must be an integer"):
        is_prime("5")
    with pytest.raises(TypeError, match="must be an integer"):
        is_prime([5])
