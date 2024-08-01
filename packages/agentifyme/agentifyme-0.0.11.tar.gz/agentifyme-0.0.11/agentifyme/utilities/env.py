import os


def load_env_file(file_path: str):
    """Load environment variables from a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist.")

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip('"').strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                os.environ[key] = value
