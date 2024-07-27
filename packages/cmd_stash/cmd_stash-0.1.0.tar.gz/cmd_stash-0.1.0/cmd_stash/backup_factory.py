from cmd_stash.backup_handlers.aws import AWSManager
from cmd_stash.backup_handlers.local import LocalBackup
from cmd_stash.backup_service import BackupService
from cmd_stash.config import ConfigManager


class BackupFactory:
    @staticmethod
    def get_instance() -> BackupService:
        """Return a backup service instance based on the provider."""
        config_manager = ConfigManager.get_instance()
        settings = config_manager.settings

        if settings is None:
            raise ValueError("Settings have not been initialized.")

        # Ensure backup_provider is not None and convert to lowercase
        if not settings.backup_provider:
            raise ValueError("Backup provider is not specified in the settings.")

        backup_provider = settings.backup_provider.lower()

        if backup_provider == "aws":
            if not settings.aws:
                raise ValueError("AWS settings are not specified in the configuration.")
            return AWSManager(settings.aws, settings.object_name)
        elif backup_provider == "local":
            if not settings.local:
                raise ValueError(
                    "Local backup settings are not specified in the configuration."
                )
            return LocalBackup(settings.local, settings.object_name)
        else:
            raise ValueError(f"Unsupported backup provider: {backup_provider}")
