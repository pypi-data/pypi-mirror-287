import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logging(level=None, log_to_file=False, log_file="cmd_stash.log"):
    """Set up logging configuration with optional file logging and rotation.

    Args:
        level (int, str, optional): Logging level. Can be passed as an integer or a string (e.g., 'DEBUG', 'INFO').
        log_to_file (bool, optional): Whether to log to a file.
        log_file (str, optional): Path to the log file.
    """
    # Create a logger
    logger = logging.getLogger()

    # Default to INFO level if not provided
    if level is None:
        level = logging.INFO  # Default to INFO level

    # Set the logging level
    logger.setLevel(level)

    # Check if console logging should be enabled
    enable_console_logging = os.getenv("ENABLE_CONSOLE_LOGGING", "false").lower() in [
        "true",
        "1",
        "t",
        "y",
        "yes",
    ]

    # Create a formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Remove existing console handlers if any
    for handler in logger.handlers[:]:
        if isinstance(handler, logging.StreamHandler):
            logger.removeHandler(handler)

    if enable_console_logging:
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    # File handler with rotation
    if log_to_file:
        file_handler = RotatingFileHandler(
            log_file, maxBytes=5 * 1024 * 1024, backupCount=5
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.debug("Logging setup complete.")
