import os
import json


def used_helper(x):
    return x * 2


def totally_unused_function_xyz(a, b):
    return a + b


if __name__ == "__main__":
    print(used_helper(3))
