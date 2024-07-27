import os
from pathlib import Path

# Get the user's home directory
home_directory = str(Path.home())

# Define default paths using the home directory
DEFAULT_COMMANDS_PATH = os.getenv(
    "CMD_COMMANDS_DIRECTORY",
    os.path.join(home_directory, ".cmd_stash", "commands.yaml"),
)
DEFAULT_CMD_STASH_LOCATION = os.getenv(
    "CMD_STASH_LOCATION", os.path.join(home_directory, ".cmd_stash")
)


# Ensure the directories exist and have appropriate permissions
def ensure_path_exists(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


ensure_path_exists(DEFAULT_COMMANDS_PATH)
ensure_path_exists(DEFAULT_CMD_STASH_LOCATION)
