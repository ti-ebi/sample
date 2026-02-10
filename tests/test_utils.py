"""Tests for utility functions."""

import sys
from pathlib import Path

# Add src to path so we can import the module
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from sample.utils import greet, add_numbers, multiply_numbers, factorial, is_prime, fibonacci, gcd


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


def test_fibonacci_base_cases():
    """Test fibonacci with base cases."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1


def test_fibonacci_small_numbers():
    """Test fibonacci with small numbers."""
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55


def test_fibonacci_larger_numbers():
    """Test fibonacci with larger numbers."""
    assert fibonacci(15) == 610
    assert fibonacci(20) == 6765
    assert fibonacci(25) == 75025
    assert fibonacci(30) == 832040


def test_fibonacci_negative():
    """Test that fibonacci raises ValueError for negative inputs."""
    import pytest
    with pytest.raises(ValueError, match="not defined for negative values"):
        fibonacci(-1)
    with pytest.raises(ValueError, match="not defined for negative values"):
        fibonacci(-10)


def test_fibonacci_non_integer():
    """Test that fibonacci raises TypeError for non-integer inputs."""
    import pytest
    with pytest.raises(TypeError, match="must be an integer"):
        fibonacci(3.5)
    with pytest.raises(TypeError, match="must be an integer"):
        fibonacci("5")
    with pytest.raises(TypeError, match="must be an integer"):
        fibonacci([5])


def test_gcd_basic_cases():
    """Test gcd with basic positive integer cases."""
    # Classic examples
    assert gcd(48, 18) == 6
    assert gcd(18, 48) == 6  # Order shouldn't matter
    assert gcd(100, 50) == 50
    assert gcd(50, 100) == 50

    # Coprime numbers (GCD = 1)
    assert gcd(17, 19) == 1
    assert gcd(13, 17) == 1
    assert gcd(7, 11) == 1

    # Same numbers
    assert gcd(42, 42) == 42
    assert gcd(1, 1) == 1


def test_gcd_with_zero():
    """Test gcd when one argument is zero."""
    # GCD of any number with 0 is the absolute value of that number
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 100) == 100
    assert gcd(100, 0) == 100


def test_gcd_with_one():
    """Test gcd with 1 as one of the arguments."""
    # GCD with 1 is always 1
    assert gcd(1, 5) == 1
    assert gcd(5, 1) == 1
    assert gcd(1, 100) == 1
    assert gcd(100, 1) == 1


def test_gcd_negative_numbers():
    """Test gcd with negative numbers."""
    # GCD should handle negative numbers and return positive result
    assert gcd(-48, 18) == 6
    assert gcd(48, -18) == 6
    assert gcd(-48, -18) == 6
    assert gcd(-100, -50) == 50


def test_gcd_large_numbers():
    """Test gcd with larger numbers."""
    assert gcd(1071, 462) == 21
    assert gcd(12345, 54321) == 3
    assert gcd(1000000, 500000) == 500000


def test_gcd_powers_of_two():
    """Test gcd with powers of two."""
    assert gcd(16, 8) == 8
    assert gcd(64, 32) == 32
    assert gcd(128, 256) == 128
    assert gcd(1024, 512) == 512


def test_gcd_both_zero():
    """Test that gcd raises ValueError when both arguments are zero."""
    import pytest
    with pytest.raises(ValueError, match="gcd\\(0, 0\\) is not defined"):
        gcd(0, 0)


def test_gcd_non_integer_first_arg():
    """Test that gcd raises TypeError when first argument is not an integer."""
    import pytest
    with pytest.raises(TypeError, match="first argument must be an integer"):
        gcd(3.5, 5)
    with pytest.raises(TypeError, match="first argument must be an integer"):
        gcd("10", 5)
    with pytest.raises(TypeError, match="first argument must be an integer"):
        gcd([10], 5)


def test_gcd_non_integer_second_arg():
    """Test that gcd raises TypeError when second argument is not an integer."""
    import pytest
    with pytest.raises(TypeError, match="second argument must be an integer"):
        gcd(5, 3.5)
    with pytest.raises(TypeError, match="second argument must be an integer"):
        gcd(5, "10")
    with pytest.raises(TypeError, match="second argument must be an integer"):
        gcd(5, [10])
