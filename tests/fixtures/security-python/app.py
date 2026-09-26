import subprocess
import os


def run_command(cmd):
    # Potential security issue: shell=True
    result = subprocess.run(cmd, shell=True, capture_output=True)
    return result.stdout


def get_env():
    return os.environ.get("SECRET_KEY", "default-secret")


run_command("ls -la")
print(get_env())
