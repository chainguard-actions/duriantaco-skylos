import os
import pickle
import subprocess
import sys


def _unused_private_helper():
    return 42


def run_command(user_input):
    os.system("echo " + user_input)
    subprocess.call(user_input, shell=True)
    return eval(user_input)


def load(data):
    return pickle.loads(data)


def main():
    run_command(sys.argv[1])
    load(sys.stdin.buffer.read())


if __name__ == "__main__":
    main()
