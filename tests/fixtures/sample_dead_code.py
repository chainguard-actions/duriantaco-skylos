"""Sample Python file with dead code for testing Skylos."""


def used_function():
    """This function is used."""
    return 42


def unused_function():
    """This function is never called - dead code."""
    return "never called"


def another_unused():
    """Another unused function."""
    pass


result = used_function()
print(result)
