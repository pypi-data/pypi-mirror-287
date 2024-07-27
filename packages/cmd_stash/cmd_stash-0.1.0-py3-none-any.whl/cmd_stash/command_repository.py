import json
import logging
from pathlib import Path
from typing import Dict

import yaml

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class CommandRepository:
    def __init__(self, file_path: Path):
        self.file_path = Path(file_path)
        self.commands = self.load_commands()

    def load_commands(self) -> Dict:
        """Load commands from a file based on its extension."""
        if self.file_path.exists():
            try:
                if self.file_path.suffix == ".json":
                    with open(self.file_path, "r") as f:
                        return json.load(f) or {}
                elif self.file_path.suffix in [".yaml", ".yml"]:
                    with open(self.file_path, "r") as f:
                        return yaml.safe_load(f) or {}
            except Exception as e:
                logger.error(f"Failed to load commands from {self.file_path}: {e}")
                raise
        return {}

    def save_commands(self):
        """Save commands to a file based on its extension."""
        try:
            if self.file_path.suffix == ".json":
                with open(self.file_path, "w") as f:
                    json.dump(self.commands, f, indent=2)
            elif self.file_path.suffix in [".yaml", ".yml"]:
                with open(self.file_path, "w") as f:
                    yaml.dump(self.commands, f, default_flow_style=False)
        except Exception as e:
            logger.error(f"Failed to save commands to {self.file_path}: {e}")
            raise

    def save_command(self, category, subcategory, description, command):
        """Save a single command into the repository."""
        if category not in self.commands:
            self.commands[category] = {}
        if subcategory not in self.commands[category]:
            self.commands[category][subcategory] = {}
        self.commands[category][subcategory][description] = command
        self.save_commands()
        logger.info(
            f"Saved command under category '{category}', subcategory '{subcategory}' with description '{description}'"
        )
        return f"Saved command: {command}"

    def list_commands(self, category, subcategory=None, description=None):
        """List commands filtered by category, subcategory, and description."""
        result = {}

        if category in self.commands:
            category_data = self.commands[category]

            if subcategory:
                if subcategory in category_data:
                    subcategory_data = category_data[subcategory]
                    result = {subcategory: subcategory_data}
                else:
                    result = {}
            else:
                result = category_data

            if description:
                result = {
                    k: {d: c for d, c in v.items() if d == description}
                    for k, v in result.items()
                }
        return result

    def list_all_commands(self):
        """List all commands."""
        return self.commands

    def export_commands(self, file_path: Path):
        """Export commands to a file based on its extension."""
        try:
            if file_path.suffix == ".json":
                with open(file_path, "w") as f:
                    json.dump(self.commands, f, indent=2)
            elif file_path.suffix in [".yaml", ".yml"]:
                with open(file_path, "w") as f:
                    yaml.dump(self.commands, f, default_flow_style=False)
            logger.info(f"Commands exported to {file_path}")
        except Exception as e:
            logger.error(f"Failed to export commands to {file_path}: {e}")
            raise

    def import_commands(self, file_path: Path):
        """Import commands from a file based on its extension."""
        try:
            if file_path.suffix == ".json":
                with open(file_path, "r") as f:
                    imported_commands = json.load(f) or {}
            elif file_path.suffix in [".yaml", ".yml"]:
                with open(file_path, "r") as f:
                    imported_commands = yaml.safe_load(f) or {}
            else:
                raise ValueError(
                    "Unsupported file format. Use '.json', '.yaml', or '.yml'."
                )

            self.commands.update(imported_commands)
            self.save_commands()
            logger.info(f"Commands imported from {file_path}")
        except Exception as e:
            logger.error(f"Failed to import commands from {file_path}: {e}")
            raise
