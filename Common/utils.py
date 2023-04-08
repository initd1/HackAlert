"""
This module has the capacity to:
  - fetch the relevant API keys of different services
  - validate keys
  - process non critical and fatal errors
  - TODO: Logging to file
"""

import logging
import sys

logger = logging.getLogger("")


def error_message(errormsg):
    logger.error(errormsg)

def exit_message(exitmsg):
    logger.critical("\033[91m{}\033[0m".format("Fatal Error: " + exitmsg))
    sys.exit(1)
