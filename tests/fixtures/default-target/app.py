"""Minimal Python application."""


def hello(name: str = "world") -> str:
    """Return a greeting."""
    return f"Hello, {name}!"


def main() -> None:
    """Entry point."""
    print(hello())


if __name__ == "__main__":
    main()
