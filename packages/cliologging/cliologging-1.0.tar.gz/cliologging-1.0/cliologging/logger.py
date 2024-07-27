from __future__ import annotations

import logging
from logging import handlers
from pathlib import Path


def get(alias: str):
        """
        Get a logger instance.
        :param alias: the logger alias.
        :return: a manipulable logger object.
        """
        return logging.getLogger(alias)


def create(alias: str, file_path: str | Path) -> logging.Logger:
    """
    Create a new logger with standard configuration for the majority project.
    :param alias: the logger alias.
    :param file_path: the access path to the recorder work file.
    :return: a manipulable logger object.
    """
    # Create logger.
    logger = logging.getLogger(alias)
    logger.setLevel(logging.DEBUG)

    # Create time rotating file handler and set level to debug.
    handler = handlers.TimedRotatingFileHandler(
        filename=file_path,
        when='D',  # Files are rotated.
        interval=1,  # Every day.
        backupCount=31,  # For one month.
        encoding='ascii',  # Use ASCII encoding.
        utc=True  # Use utc timestamp.
    )
    handler.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter(
        fmt="%(process)d %(asctime)s %(levelname)-8s In:%(module)s|%(lineno)d : %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z"
    )

    # Add formatter to handler
    handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(handler)

    return logger  # Return logger object.
