import pickle
import subprocess
import sys


def run(cmd):
    return subprocess.call(cmd, shell=True)


def evaluate(expr):
    return eval(expr)


def load(data):
    return pickle.loads(data)


if __name__ == "__main__":
    user = sys.argv[1] if len(sys.argv) > 1 else input()
    run(user)
    print(evaluate(user))
    load(user.encode())
