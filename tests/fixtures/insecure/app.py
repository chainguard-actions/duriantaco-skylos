import subprocess


def run(user_input):
    eval(user_input)
    subprocess.call(user_input, shell=True)


if __name__ == "__main__":
    run(input())
