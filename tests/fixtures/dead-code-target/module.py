"""Module with some dead code for detection testing."""


def used_function() -> str:
    """This function is used."""
    return "used"


def _unused_helper() -> str:
    """This function is never called."""
    return "unused"


def main() -> None:
    """Entry point."""
    result = used_function()
    print(result)


if __name__ == "__main__":
    main()
