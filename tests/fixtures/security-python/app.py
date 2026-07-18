import subprocess
import os


def run_command(user_input):
    # Potential security issue: shell injection
    result = subprocess.run(user_input, shell=True, capture_output=True)
    return result.stdout


def get_env():
    return os.environ.get("SECRET_KEY", "default-secret")


if __name__ == "__main__":
    print(get_env())
