"""Sample Python module for Skylos scan testing."""


def used_function():
    """This function is used."""
    return "hello"


def unused_function():
    """This function is never called - potential dead code."""
    return "world"


def main():
    result = used_function()
    print(result)


if __name__ == "__main__":
    main()
