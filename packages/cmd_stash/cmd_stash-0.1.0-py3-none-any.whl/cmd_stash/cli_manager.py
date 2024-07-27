import json
import logging
from pathlib import Path

import click
import yaml

from cmd_stash.backup_factory import BackupFactory
from cmd_stash.backup_service import BackupCreationException, BackupDestructionException
from cmd_stash.command_repository import CommandRepository
from cmd_stash.config import ConfigManager
from cmd_stash.logging_config import setup_logging

# Set up logging
setup_logging(level=logging.DEBUG, log_to_file=True, log_file="cli_manager.log")
logger = logging.getLogger(__name__)


class CLIManager:
    """CLI Manager to handle command line interactions."""

    def __init__(self):
        self.config_manager = ConfigManager.get_instance()
        self.settings = self.config_manager.get_settings()
        self.backup_service = BackupFactory.get_instance()
        self.location = self.settings.commands_file
        self.resource_name = self.config_manager.get_resource_name()
        self.object_name = self.settings.object_name
        self.initialize_location(self.location)
        self.cli = click.Group()

        # Register commands
        self.cli.add_command(self.set_config())
        self.cli.add_command(self.show_config())
        self.cli.add_command(self.set_location())
        self.cli.add_command(self.save_command())
        self.cli.add_command(self.list_commands())
        self.cli.add_command(self.list_all_commands())
        self.cli.add_command(self.import_commands())
        self.cli.add_command(self.create_backup())
        self.cli.add_command(self.destroy_backup())
        self.cli.add_command(self.backup())
        self.cli.add_command(self.restore())

    def initialize_location(self, location):
        """Ensure the location path exists and create it if necessary."""
        path = Path(location)
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
        return str(path)

    def set_config(self):
        """Set or update the path to the configuration file."""

        @click.command(name="set-config")
        @click.argument(
            "config", type=click.Path(exists=True, dir_okay=False, file_okay=True)
        )
        def set_config_command(config):
            config_path = Path(config).resolve()

            if not config_path.is_absolute():
                click.echo(f"Error: The path '{config_path}' is not an absolute path.")
                raise click.UsageError("Please provide an absolute path.")

            self.config_manager.save_persisted_settings(config_path)
            click.echo(
                f"Configuration path saved to {Path.home() / '.cmd_stash' / 'cli_settings.yaml'}"
            )
            click.echo(f"Configuration path set to: {config_path}")

        return set_config_command

    def show_config(self):
        """Display the current configuration details."""

        @click.command(name="show-config")
        def show_config_command():
            config_details = self.config_manager.get_configuration_details()
            if config_details:
                click.echo("Configuration details:")
                click.echo(json.dumps(config_details, indent=2))
            elif self.config_manager.default_config_path.exists():
                config = self.config_manager.load_yaml_config(
                    self.config_manager.default_config_path
                )
                click.echo(
                    f"Using default configuration from {self.config_manager.default_config_path}"
                )
                click.echo(json.dumps(config, indent=2))
            else:
                click.echo("Using default configuration.")
                click.echo(json.dumps({"default": "config"}, indent=2))

        return show_config_command

    def set_location(self):
        """Set or update the location of the commands file."""

        @click.command(name="set-location")
        @click.argument(
            "location", type=click.Path(exists=False, dir_okay=True, file_okay=True)
        )
        def set_location_command(location):
            self.location = str(Path(location))
            Path(self.location).touch()
            click.echo(f"Commands file location set to: {self.location}")

        return set_location_command

    def save_command(self):
        """Save a command with the given category, subcategory, and description."""

        @click.command(name="save")
        @click.argument("category")
        @click.argument("subcategory")
        @click.argument("description")
        @click.argument("command", nargs=-1)
        def save_command(category, subcategory, description, command):
            cmd_stash = CommandRepository(file_path=self.location)
            try:
                command_str = " ".join(command)
                result = cmd_stash.save_command(
                    category, subcategory, description, command_str
                )
                click.echo(f"Saved command: {result}")
            except ValueError as e:
                click.echo(f"Error: {e}")
                logger.error("Error saving command: %s", e)

        return save_command

    def list_commands(self):
        """List all commands under a category, optionally filtered by subcategory and description."""

        @click.command(name="list")
        @click.argument("category")
        @click.argument("subcategory", default=None, required=False)
        @click.option("--description", default=None, help="Filter by description")
        def list_commands_command(category, subcategory, description):
            cmd_stash = CommandRepository(file_path=self.location)
            try:
                result = cmd_stash.list_commands(category, subcategory, description)
                click.echo(json.dumps(result, indent=2))
            except ValueError as e:
                click.echo(f"Error: {e}")
                logger.error("Error listing commands: %s", e)

        return list_commands_command

    def list_all_commands(self):
        """List all commands."""

        @click.command(name="list-all")
        def list_all_commands_command():
            cmd_stash = CommandRepository(file_path=self.location)
            try:
                result = cmd_stash.list_all_commands()
                click.echo(json.dumps(result, indent=2))
            except ValueError as e:
                click.echo(f"Error: {e}")
                logger.error("Error listing commands: %s", e)

        return list_all_commands_command

    def import_commands(self):
        """Import commands from a JSON or YAML file."""

        @click.command(name="import")
        @click.argument("file_path", type=click.Path(dir_okay=False, file_okay=True))
        def import_commands_command(file_path):
            file_path = Path(file_path)
            if not file_path.is_file():
                click.echo(
                    f"Error: The file {file_path} does not exist or is not a valid file."
                )
                logger.error(
                    "File %s does not exist or is not a valid file.", file_path
                )
                return
            try:
                cmd_stash = CommandRepository(file_path=self.location)
                cmd_stash.import_commands(file_path)
                click.echo(f"Commands imported from {file_path}")
            except (OSError, IOError, json.JSONDecodeError, yaml.YAMLError) as e:
                click.echo(f"Error importing commands: {e}")
                logger.error("Error importing commands from %s: %s", file_path, e)
            except ValueError as e:
                click.echo(f"Error: {e}")
                logger.error("Error importing commands: %s", e)

        return import_commands_command

    def create_backup(self):
        """Create a backup."""

        @click.command(name="create-backup")
        def create_backup_command():
            try:
                result = self.backup_service.create_backup(self.resource_name)
                click.echo(result)
            except BackupCreationException as e:
                click.echo(f"Error creating backup: {e}")
                logger.error("Error creating backup: %s", e)
            except Exception as e:
                click.echo(f"Unexpected error: {e}")
                logger.error("Unexpected error: %s", e)

        return create_backup_command

    def destroy_backup(self):
        """Destroy a backup."""

        @click.command(name="destroy-backup")
        @click.argument("resource_name")
        @click.confirmation_option(
            prompt="Are you sure you want to destroy the backup?"
        )
        def destroy_backup_command(resource_name):
            """Command function to destroy the backup."""
            try:
                result = self.backup_service.destroy_backup(resource_name)
                click.echo(result)
            except BackupDestructionException as e:
                click.echo(f"Error destroying backup: {e}")
                logger.error("Error destroying backup: %s", e)
            except Exception as e:
                click.echo(f"Unexpected error: {e}")
                logger.error("Unexpected error: %s", e)

        return destroy_backup_command

    def backup(self):
        """Backup a file."""

        @click.command(name="backup")
        def backup_command():
            if not self.backup_service.backup_exists(self.resource_name):
                click.echo(
                    f"Error: The backup resource '{self.resource_name}' does not exist."
                )
                logger.warning(
                    "Backup resource '%s' does not exist.", self.resource_name
                )
                return
            try:
                result = self.backup_service.backup(
                    self.location, self.resource_name, self.object_name
                )
                click.echo(result)
            except Exception as e:
                click.echo(f"Error during backup: {e}")
                logger.error("Error during backup: %s", e)

        return backup_command

    def restore(self):
        """Restore a file."""

        @click.command(name="restore")
        @click.confirmation_option(
            prompt="Are you sure you want to restore the backup?"
        )
        def restore_command():
            if not self.backup_service.backup_exists(self.resource_name):
                click.echo(
                    f"Error: The backup resource '{self.resource_name}' does not exist."
                )
                logger.warning(
                    "Backup resource '%s' does not exist.", self.resource_name
                )
                return
            try:
                result = self.backup_service.restore(
                    self.resource_name, self.object_name, self.location
                )
                click.echo(result)
            except Exception as e:
                click.echo(f"Error during restore: {e}")
                logger.error("Error during restore: %s", e)

        return restore_command


def cli():
    """Entry point for the CLI commands."""
    setup_logging(level=logging.DEBUG, log_to_file=True)

    cli_manager = CLIManager()
    cli_manager.cli()


if __name__ == "__main__":
    cli()
