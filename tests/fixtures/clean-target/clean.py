"""A clean Python module with no dead code or security issues."""


def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


def main() -> None:
    """Entry point."""
    result = add(2, 3)
    product = multiply(result, 2)
    print(f"Result: {product}")


if __name__ == "__main__":
    main()
