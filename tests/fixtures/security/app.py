import subprocess


def run_command(user_input):
    # Potential security issue: shell injection
    result = subprocess.run(user_input, shell=True, capture_output=True)
    return result.stdout


def safe_function():
    return "hello world"
