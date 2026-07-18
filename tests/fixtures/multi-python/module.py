import os
import sys


def used_function(x):
    return x * 2


def dead_function():
    """This function is never called."""
    pass


class MyClass:
    def __init__(self):
        self.value = 42

    def get_value(self):
        return self.value


if __name__ == "__main__":
    obj = MyClass()
    print(used_function(obj.get_value()))
