"""A minimal clean Python module with no dead code or security issues."""


def greet(name: str) -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"


def main() -> None:
    """Entry point."""
    message = greet("world")
    print(message)


if __name__ == "__main__":
    main()
