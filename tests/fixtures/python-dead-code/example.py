def active_function():
    """This function is called."""
    return "active"


def dead_function():
    """This function is never called - dead code."""
    return "dead"


def another_dead_function():
    """Another unused function."""
    x = 10
    return x * 2


# Only active_function is called
print(active_function())
