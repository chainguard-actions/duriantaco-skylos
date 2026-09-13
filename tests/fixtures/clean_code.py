"""Clean Python file with no issues for testing Skylos."""


def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}!"


def main():
    """Main entry point."""
    message = greet("World")
    print(message)


if __name__ == "__main__":
    main()
