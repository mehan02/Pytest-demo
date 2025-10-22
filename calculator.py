# calculator.py - Enhanced module for unit testing (own code)
import math


def add(a, b):
    """Add two numbers"""
    return a + b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def power(base, exponent):
    """Raise base to the given exponent"""
    return base ** exponent


def square_root(x):
    """Return the square root of x"""
    if x < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(x)


class Calculator:
    """Basic calculator class"""

    def divide(self, a, b):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def average(self, numbers):
        """Compute average of a list of numbers"""
        if not numbers:
            raise ValueError("Cannot compute average of empty list")
        return sum(numbers) / len(numbers)
