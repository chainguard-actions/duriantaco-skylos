"""A Python module with intentional dead code for testing."""


def used_function(x: int) -> int:
    """This function is used."""
    return x * 2


def _unused_helper(data):
    """This function is never called anywhere - dead code."""
    result = []
    for item in data:
        result.append(item)
    return result


def another_unused(value):
    """Another unused function."""
    return value + 100


if __name__ == "__main__":
    print(used_function(5))
