"""Utility functions for the sample project."""


def greet(name: str) -> str:
    """
    Generate a greeting message.

    Args:
        name: The name to greet.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"


def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The sum of a and b.
    """
    return a + b


def multiply_numbers(a: int, b: int) -> int:
    """
    Multiply two numbers together.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The product of a and b.
    """
    return a * b


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    The factorial of n (written as n!) is the product of all positive
    integers less than or equal to n. For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.
    By definition, 0! = 1.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n.

    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError(f"factorial() argument must be an integer, not {type(n).__name__}")
    if n < 0:
        raise ValueError("factorial() not defined for negative values")

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
