import json
import logging
import shutil
from datetime import datetime
from pathlib import Path

from cmd_stash.backup_service import BackupService
from cmd_stash.config import LocalConfig

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class LocalBackup(BackupService):
    def __init__(self, config: LocalConfig, object_name: str):
        """Initialize the LocalBackup service with configuration."""
        self.config = config
        self.object_name = object_name

        # Convert config directory and directory_name to Path objects if they are strings
        self.directory = (
            Path(self.config.directory)
            if isinstance(self.config.directory, str)
            else self.config.directory
        )
        self.directory_name = (
            Path(self.config.directory_name)
            if isinstance(self.config.directory_name, str)
            else self.config.directory_name
        )
        self.location = self.directory / self.directory_name

        # Ensure the backup directory exists
        self.location.mkdir(parents=True, exist_ok=True)

        logger.debug(f"Backup location initialized at {self.location}")
        logger.debug(f"Object name for backup set to {self.object_name}")

    def create_backup(self, resource_name: str) -> str:
        """Create a backup directory and initialize it with an empty file."""
        backup_dir = self.location / resource_name
        logger.debug(f"Creating backup directory at: {backup_dir}")

        # Ensure the directory for the backup exists
        backup_dir.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Backup directory created or already exists: {backup_dir}")

        # Create the object_name file inside the directory
        object_path = backup_dir / self.object_name
        logger.debug(f"Creating object file at: {object_path}")

        # Create an empty file or initialize it with some default content
        with object_path.open("w") as file:
            json.dump(
                {}, file
            )  # Create an empty JSON file or initialize with default content

        message = f"Backup directory for {resource_name} created at {backup_dir}, with file {self.object_name}."
        logger.info(message)
        return message

    def backup_exists(self, resource_name: str) -> bool:
        """Check if the backup directory for the resource exists."""
        backup_dir = self.location / resource_name
        exists = backup_dir.exists()
        logger.debug(
            f"Backup existence check for {resource_name}: {'exists' if exists else 'does not exist'}"
        )
        return exists

    def backup(self, file_path: str, resource_name: str, key: str) -> str:
        """Backup a file to the specified directory."""
        logger.debug(
            f"Starting backup process for file_path: {file_path}, resource_name: {resource_name}, key: {key}"
        )

        backup_dir = self.location / resource_name
        logger.debug(f"Backup directory path: {backup_dir}")

        # Ensure the backup directory exists
        backup_dir.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Ensured existence of backup directory: {backup_dir}")

        # Use the object_name from settings as the base filename
        base_filename = self.object_name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_key = f"{base_filename.split('.')[0]}_{timestamp}.txt"
        destination_path = backup_dir / new_key
        logger.debug(f"New backup file path: {destination_path}")

        # Copy the file to the backup directory
        shutil.copy(file_path, destination_path)
        logger.debug(f"Copied file from {file_path} to {destination_path}")

        message = f"File {file_path} backed up to {destination_path}."
        logger.info(message)
        return message

    def restore(self, resource_name: str, key: str, local_path: str) -> str:
        """Restore a file from the backup to a local path."""
        backup_dir = self.location / resource_name
        source_path = backup_dir / key

        # Ensure both paths are strings
        source_path_str = (
            str(source_path) if isinstance(source_path, Path) else source_path
        )
        local_path_str = str(local_path) if isinstance(local_path, Path) else local_path

        logger.debug(f"Restoring file from {source_path_str} to {local_path_str}")

        if not source_path.exists():
            logger.error(f"Source file does not exist: {source_path_str}")
            raise FileNotFoundError(f"Source file does not exist: {source_path_str}")

        shutil.copy(source_path_str, local_path_str)
        logger.debug(f"Restored file to {local_path_str}")

        message = f"File {source_path_str} restored to {local_path_str}."
        logger.info(message)
        return message

    def destroy_backup(self, resource_name: str) -> str:
        """Destroy the backup directory."""
        backup_dir = self.location / resource_name
        logger.debug(f"Attempting to delete backup directory: {backup_dir}")

        if backup_dir.exists():
            shutil.rmtree(backup_dir)
            message = f"Backup directory for {resource_name} deleted."
            logger.info(message)
            return message
        else:
            message = f"Backup directory for {resource_name} does not exist."
            logger.warning(message)
            return message
