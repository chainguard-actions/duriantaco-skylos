"""Module with security issues for detection testing."""
import subprocess
import os


def run_command(cmd: str) -> str:
    """Run a shell command (insecure: shell=True)."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout


def evaluate_expression(expr: str) -> object:
    """Evaluate a Python expression (insecure: eval)."""
    return eval(expr)  # noqa


def main() -> None:
    """Entry point."""
    output = run_command("echo hello")
    print(output)
    value = evaluate_expression("1 + 1")
    print(value)


if __name__ == "__main__":
    main()
