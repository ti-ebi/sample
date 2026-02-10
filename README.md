# Sample Python Project

A clean, well-structured Python project template demonstrating best practices for code organization, testing, and documentation.

## Features

- Clean project structure following Python best practices
- Unit tests with pytest
- Example utility functions
- Simple and extensible

## Project Structure

```
.
├── README.md
├── requirements.txt
├── setup.py
├── src/
│   └── sample/
│       ├── __init__.py
│       └── utils.py
└── tests/
    ├── __init__.py
    └── test_utils.py
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from sample.utils import greet, add_numbers, multiply_numbers, factorial, is_prime, fibonacci, gcd

# Use the greeting function
message = greet("World")
print(message)  # Output: Hello, World!

# Perform calculations
result = add_numbers(5, 3)
print(result)  # Output: 8

product = multiply_numbers(4, 7)
print(product)  # Output: 28

# Calculate factorial
fact = factorial(5)
print(fact)  # Output: 120

# Check if a number is prime
print(is_prime(17))  # Output: True
print(is_prime(20))  # Output: False

# Calculate Fibonacci numbers
print(fibonacci(10))  # Output: 55
print(fibonacci(15))  # Output: 610

# Calculate the Greatest Common Divisor
print(gcd(48, 18))  # Output: 6
print(gcd(100, 50))  # Output: 50
```

## Running Tests

```bash
pytest tests/
```

## Development

This project serves as a template for Python development. Feel free to extend it with your own functionality.

## License

MIT
