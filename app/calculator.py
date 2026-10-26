"""Simple calculator functions. Ye sample code hai, apne project ke code se replace kar sakte ho."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Zero se divide nahi kar sakte")
    return a / b
