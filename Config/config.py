import configparser
import logging.config
from Common import utils


def configure_logging(file="config.ini"):
    """Set up default logger for logging messages.

    :param `file`: File to set configuration from.
    """

    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
    except Exception as er:
        utils.error_message(er)
    finally:
        logging.config.fileConfig(file)
    return
