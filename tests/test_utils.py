"""Tests for utility functions."""

import sys
from pathlib import Path

# Add src to path so we can import the module
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from sample.utils import greet, add_numbers, multiply_numbers


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
