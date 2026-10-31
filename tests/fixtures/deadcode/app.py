import os


def used_function(value):
    return value * 2


def never_called_helper(value):
    return value + 42


if __name__ == "__main__":
    print(used_function(3))
