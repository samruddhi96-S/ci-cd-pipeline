"""Simple text utility functions for CI/CD testing."""

def reverse_string(text):
    """Reverses the given string."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[::-1]

def count_words(text):
    """Counts the number of words in a string."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return len(text.split())

if __name__ == "__main__":
    print("Testing Text Utilities:")
    print(reverse_string("Hello CI/CD"))
    print(count_words("Hello CI/CD Pipeline"))