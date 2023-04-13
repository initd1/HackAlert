import logging
import logging.config
import configparser
import os
import sys


def get_config(config_file_path):
    """
    Parse configuration from file and environment variables.

    :param str config_file_path: path to the configuration file
    :return: configuration values as a dictionary
    :rtype: dict
    """
    config = configparser.ConfigParser()

    # read from file
    config.read(config_file_path, encoding="utf-8")
    config.__dict__

    # read from environment variables
    for key in config["ENVIRONMENT"]:
        env_var = os.environ.get(key)
        if env_var is not None:
            config["ENVIRONMENT"][key] = env_var

    return config


def get_logging_config(file_location="Config/logger.ini"):
    """
    Get logging configuration from configuration file.

    :return: logging configuration as a dictionary
    :rtype: dict
    """
    try:
        open(file_location, "r")
    except FileNotFoundError:
        logging.critical(f"File location invalid: {file_location}")
        sys.exit(1)

    config = get_config("Config/logger.ini")
    return config


def configure_logging():
    """
    Configure logging for the application.
    """
    logging_config = get_logging_config()
    return logging_config
