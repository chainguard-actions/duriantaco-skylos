import os
import subprocess


def run_user_code():
    user_input = input("code: ")
    return eval(user_input)


def run_shell():
    cmd = input("cmd: ")
    os.system(cmd)
    subprocess.call(cmd, shell=True)


def main():
    run_user_code()
    run_shell()


if __name__ == "__main__":
    main()
