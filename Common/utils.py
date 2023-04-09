"""
This module has the capacity to:
  - fetch the relevant API keys of different services
  - validate keys
  - process non critical and fatal errors
  - TODO: Logging to file
"""

import json
import logging
import sys
import requests

logger = logging.getLogger("")


def error_message(error_msg):
    """Logs error message; displays `error_msg`

    :param error_msg: Message to display as error with a log level of *error*.
    """

    logger.error(error_msg)

def exit_message(exit_msg, error_code=1):
    """Halt runtime and exit with `error_code` (default=1)

    :param exit_msg: Display this message when exiting with a log level of *critical*.
    """

    logger.critical("\033[91m{}\033[0m".format(f"Fatal Error: {exit_msg}"))
    sys.exit(error_code)

def check_VTAPIkey(key):
    """Checks if the VirusTotal API Key is valid.

    :param key: VirusTotal API key as defined (manually) in configuration ini file.
    :return: The validity of `key`
    :rtype: bool
    """

    # Google IP for validating key
    ip = "8.8.8.8"
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": key}
    response = requests.request("GET", url, headers=headers, data={}).text
    data = json.loads(response)

    if "error" not in data:
        logger.info("Virus Total Key Validation: \033[92m{}\033[0m".format("Success"))
        return True
    else:
        error_message(json.dumps(data["error"], indent=4, sort_keys=True))
        exit_message("Virus Total Key Validation failed")
        return False
