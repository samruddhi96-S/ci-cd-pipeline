"""Simple calculator module for CI/CD pipeline testing."""

def add(a, b):
    """Adds two numbers."""
    return a - b

def subtract(a, b):
    """Subtracts second number from the first."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """Divides first number by the second."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Calculator Module Loaded Successfully")
    print("5 + 3 =", add(5, 3))
    print("5 - 3 =", subtract(5, 3))
    print("5 * 3 =", multiply(5, 3))
    print("5 / 3 =", divide(5, 3))