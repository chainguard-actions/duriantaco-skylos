import os


def get_config():
    """Read configuration."""
    return {
        "host": os.environ.get("DB_HOST", "localhost"),
        "port": int(os.environ.get("DB_PORT", "5432")),
    }


def connect(config):
    """Connect to database."""
    host = config["host"]
    port = config["port"]
    return f"Connected to {host}:{port}"


if __name__ == "__main__":
    cfg = get_config()
    print(connect(cfg))
