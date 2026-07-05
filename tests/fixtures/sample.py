# Sample Python file for Skylos scan testing
# This file is intentionally simple and clean

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


if __name__ == "__main__":
    print(greet("world"))
    print(add(1, 2))
