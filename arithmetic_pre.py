"""Math functions for calculator."""


def add(num):
    """Return the sum of the list of inputs."""
    total = 0
    for i in num:
        total = total + i
    return total


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return num1 - num2


def multiply(num1, num2):
    """Multiply the two inputs together."""
    total = 1
    for i in num:
        total = total * i
    return total


def divide(num1, num2):
    """Divide the first input by the second and return the result."""

    return float(num1) / num2


def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
