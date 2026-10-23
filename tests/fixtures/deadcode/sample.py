import os
import json


def used_function(value):
    return value * 2


def totally_unused_helper(a, b):
    return a + b


class NeverInstantiatedThing:
    def never_called_method(self):
        return "nope"


if __name__ == "__main__":
    print(used_function(21))
