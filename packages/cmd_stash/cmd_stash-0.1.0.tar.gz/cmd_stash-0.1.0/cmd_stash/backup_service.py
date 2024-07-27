from abc import ABC, abstractmethod


class BackupException(Exception):
    """Base exception class for backup-related errors."""

    pass


class BackupCreationException(BackupException):
    """Exception raised for errors during backup creation."""

    pass


class BackupDestructionException(BackupException):
    """Exception raised for errors during backup destruction."""

    pass


class BackupNotFoundException(BackupException):
    """Exception raised when a backup resource is not found."""

    pass


class BackupService(ABC):
    @abstractmethod
    def create_backup(self, resource_name: str) -> str:
        """Create a backup for the specified resource."""
        pass

    @abstractmethod
    def backup_exists(self, resource_name: str) -> bool:
        """Check if a backup for the specified resource exists."""
        pass

    @abstractmethod
    def backup(self, file_path: str, resource_name: str, key: str) -> str:
        """Upload a file as a backup to the specified resource."""
        pass

    @abstractmethod
    def restore(self, resource_name: str, key: str, local_path: str) -> str:
        """Restore a file from the specified resource."""
        pass

    @abstractmethod
    def destroy_backup(self, resource_name: str) -> str:
        """Delete the backup for the specified resource."""
        pass
