"""A Python module with obvious dead code for testing."""


def used_function() -> str:
    """This function is used."""
    return "I am used"


def _unused_private_function() -> str:
    """This function is never called anywhere - dead code."""
    return "I am never called"


def another_unused() -> int:
    """Another unused function."""
    return 42


def main() -> None:
    """Entry point."""
    result = used_function()
    print(result)


if __name__ == "__main__":
    main()
