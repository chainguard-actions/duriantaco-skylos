import os
import subprocess


def unused_helper_function():
    return 42


def run_user_code():
    user_input = input("code: ")
    eval(user_input)
    subprocess.call(user_input, shell=True)


def main():
    run_user_code()


if __name__ == "__main__":
    main()
