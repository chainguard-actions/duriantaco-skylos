import os
import json


def used_function():
    return 1


def completely_unused_helper_function():
    return json.dumps({"a": 1})


def main():
    print(used_function())


if __name__ == "__main__":
    main()
