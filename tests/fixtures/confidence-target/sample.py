"""Sample module for confidence threshold testing."""
import subprocess


def process_data(data: list) -> list:
    """Process a list of data items."""
    return [item for item in data if item]


def run_shell(cmd: str) -> str:
    """Run a shell command."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout


def _internal_helper(x: int) -> int:
    """Internal helper that may be unused."""
    return x * 2


def main() -> None:
    """Entry point."""
    items = process_data([1, 2, None, 3])
    print(items)
    output = run_shell("echo test")
    print(output)


if __name__ == "__main__":
    main()
