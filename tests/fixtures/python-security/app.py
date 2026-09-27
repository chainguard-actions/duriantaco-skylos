import subprocess
import os


def run_command(cmd):
    """Run a shell command."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout


def get_env(key):
    return os.environ.get(key, "")


if __name__ == "__main__":
    print(run_command("echo hello"))
