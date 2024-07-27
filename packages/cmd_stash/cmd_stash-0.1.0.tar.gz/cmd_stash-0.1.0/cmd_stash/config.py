import logging
import os
from pathlib import Path
from typing import Any, Dict, Optional

import yaml
from pydantic import BaseModel, Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

from cmd_stash.constants import DEFAULT_CMD_STASH_LOCATION, DEFAULT_COMMANDS_PATH

logger = logging.getLogger(__name__)


class AWSConfig(BaseModel):
    region: str = Field(default="us-east-1", description="AWS region")
    bucket_name: str = Field(default="cmd-stash-bucket", description="S3 bucket name")
    bucket_acl: str = Field(default="private", description="S3 bucket ACL")


class LocalConfig(BaseModel):
    directory: str = Field(
        default=DEFAULT_COMMANDS_PATH, description="Local backup directory"
    )
    directory_name: str = Field(
        default="backups", description="Name of the directory for backups"
    )


class AppSettings(BaseSettings):
    commands_file: Path = Field(
        default=DEFAULT_COMMANDS_PATH, description="Path to the commands file"
    )
    backup_provider: Optional[str] = Field(
        default="local", description="Backup provider (e.g., aws, local)"
    )
    object_name: str = Field(
        default="commands.json", description="Name of the resource to backup"
    )
    backup_providers: Optional[Dict[str, Any]] = None

    @property
    def aws(self) -> Optional[AWSConfig]:
        """Get the AWS configuration if the backup provider is AWS."""
        if self.backup_provider == "aws" and self.backup_providers:
            return AWSConfig(**self.backup_providers.get("aws", {}))
        return None

    @property
    def local(self) -> Optional[LocalConfig]:
        """Get the local configuration if the backup provider is local."""
        if self.backup_provider == "local" and self.backup_providers:
            return LocalConfig(**self.backup_providers.get("local", {}))
        return None

    model_config = SettingsConfigDict(env_prefix="CMD_", extra="forbid")


class ConfigManager:
    _instance: Optional["ConfigManager"] = None
    __initialized: bool = False
    settings_path: Optional[Path] = None
    settings: Optional[AppSettings] = None

    def __new__(cls, settings_path: Optional[Path] = None) -> "ConfigManager":
        """Create a new instance of ConfigManager if it doesn't exist."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.settings_path = settings_path
        return cls._instance

    def __init__(self, settings_path: Optional[Path] = None) -> None:
        """Initialize the ConfigManager instance."""
        if self.__initialized:
            return
        self.settings_path = settings_path
        self.settings = self.get_settings()
        self.__initialized = True

    @classmethod
    def get_instance(cls, settings_path: Optional[Path] = None) -> "ConfigManager":
        """Get the singleton instance of ConfigManager."""
        if cls._instance is None:
            cls._instance = cls(settings_path=settings_path)
        return cls._instance

    def load_yaml_config(self, path: Path) -> Dict[str, Any]:
        """Load YAML configuration from the specified path."""
        with path.open("r") as file:
            data = yaml.safe_load(file)
            if not isinstance(data, dict):
                raise ValueError(
                    "YAML configuration file does not contain a dictionary"
                )
            return data

    def filter_valid_fields(
        self, settings_dict: Dict[str, Any], model: BaseSettings
    ) -> Dict[str, Any]:
        """Filter out invalid fields based on the model's annotations."""
        valid_fields = set(model.__annotations__.keys())
        return {
            key: value for key, value in settings_dict.items() if key in valid_fields
        }

    def get_settings(self) -> AppSettings:
        """Retrieve settings by loading from the specified configuration path."""
        user_settings_path = Path.home() / ".cmd_stash" / "cli_settings.yaml"

        logger.debug("User settings path: %s", user_settings_path)

        primary_config_path: Optional[Path] = None

        if user_settings_path.exists():
            settings_from_cli = self.load_yaml_config(user_settings_path)
            primary_config_path = Path(settings_from_cli.get("config_path", ""))
            logger.debug(
                "Primary config path from CLI settings: %s", primary_config_path
            )
        elif self.settings_path:
            primary_config_path = self.settings_path

        settings_dict: Dict[str, Any] = {
            "commands_file": "default_commands_file_path",
            "backup_provider": "local",  # or any default provider
            "object_name": "commands.json",
            "backup_providers": {
                "local": {
                    "directory": DEFAULT_CMD_STASH_LOCATION,
                    "directory_name": "backups",
                }
            },
        }

        if primary_config_path and primary_config_path.exists():
            yaml_config = self.load_yaml_config(primary_config_path)
            logger.debug("Loaded settings from %s", primary_config_path)
            settings_dict.update(yaml_config)  # Merge YAML config with default settings

        # Update with environment variables
        env_config = {
            key: value for key, value in os.environ.items() if key.startswith("CMD_")
        }
        settings_dict.update(env_config)

        settings_dict = self.filter_valid_fields(settings_dict, AppSettings())

        # Ensure commands_file has a default value if it's not provided
        if "commands_file" not in settings_dict:
            settings_dict["commands_file"] = (
                "default_commands_file_path"  # Adjust default path if necessary
            )

        try:
            return AppSettings(**settings_dict)
        except ValidationError as e:
            logger.error("Configuration validation error: %s", e)
            raise
        except Exception as e:
            logger.error("An unexpected error occurred: %s", e)
            raise

    def save_persisted_settings(self, config_path: Path) -> None:
        """Save the specified configuration path to a persistent settings file."""
        settings_dir = Path.home() / ".cmd_stash"
        settings_dir.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists

        settings_file = settings_dir / "cli_settings.yaml"

        # Write the new configuration path to the file
        with settings_file.open("w") as file:
            yaml.safe_dump({"config_path": str(config_path)}, file)
        print(f"Configuration path saved to {settings_file}")

    def update_settings(self, config_path: Path) -> AppSettings:
        """Update settings based on a new configuration file."""
        try:
            yaml_config = self.load_yaml_config(config_path)
            settings_dict = self.filter_valid_fields(yaml_config, AppSettings())
            return AppSettings(**settings_dict)
        except ValidationError as e:
            logger.error("Configuration validation error: %s", e)
            raise
        except Exception as e:
            logger.error("An unexpected error occurred: %s", e)
            raise

    def get_resource_name(self) -> str:
        """Determine the resource name based on the backup provider."""
        if not self.settings:
            raise ValueError("Settings have not been initialized.")

        if self.settings.backup_provider == "aws":
            return self.settings.aws.bucket_name if self.settings.aws else ""
        elif self.settings.backup_provider == "local":
            return self.settings.local.directory_name if self.settings.local else ""
        else:
            raise ValueError(
                f"Unsupported backup provider: {self.settings.backup_provider}"
            )

    def get_backup_provider(self) -> str:
        """Return the backup provider."""
        if not self.settings:
            return "unknown"

        return self.settings.backup_provider or "unknown"

    def get_configuration_details(self) -> Dict[str, Any]:
        """Return the configuration details as a dictionary."""
        settings = self.get_settings()

        config_details: Dict[str, Any] = {
            "backup_provider": settings.backup_provider,
            "commands_file": str(settings.commands_file),
            "object_name": settings.object_name,
        }

        if settings.aws:
            config_details["aws"] = {
                "region": settings.aws.region,
                "bucket_name": settings.aws.bucket_name,
                "bucket_acl": settings.aws.bucket_acl,
            }

        if settings.local:
            config_details["local"] = {
                "directory": settings.local.directory,
                "directory_name": settings.local.directory_name,
            }

        return config_details
