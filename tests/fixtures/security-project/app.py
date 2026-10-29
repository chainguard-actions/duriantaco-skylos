import os
import pickle
import subprocess


def run_command(user_input):
    subprocess.call(user_input, shell=True)
    os.system("ls " + user_input)
    return eval(user_input)


def load(data):
    return pickle.loads(data)


if __name__ == "__main__":
    cmd = input("cmd: ")
    run_command(cmd)
    load(cmd.encode())
