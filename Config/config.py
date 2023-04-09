# FILE CURRENTLY NOT USED

# import configparser
# from Common import utils

# try:
#     config = configparser.ConfigParser()
#     config.read('config.ini')
# except Exception as er:
#     utils.error_message(er)

# # Get the Virus Total API key from the config file
# VT_APIKey = config['APIKeys']['VT_APIKey']
import logging.config


def configure_logging(file="config.ini"):
    """Set up default logger for logging messages.

    :param `file`: File to set configuration from.
    """

    logging.config.fileConfig(file)
