import json
import collections


def used_function(x):
    return x * 2


def completely_unused_helper(value):
    return value + 42


def another_unused_function_never_called():
    return "nobody calls me"


class UnusedClassNeverReferenced:
    def method(self):
        return 1


if __name__ == "__main__":
    print(used_function(3))
