import os
import json


def used_function():
    return 1


def totally_unused_helper_function():
    return os.getcwd()


def another_unused_function(value):
    return value * 2


print(used_function())
