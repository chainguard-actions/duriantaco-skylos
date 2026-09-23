"""A minimal Python module for testing Skylos scanning."""


def greet(name: str) -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


def main() -> None:
    """Entry point."""
    message = greet("world")
    result = add(1, 2)
    print(message)
    print(f"1 + 2 = {result}")


if __name__ == "__main__":
    main()
