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


def error_message(errormsg):
    logger.error(errormsg)


def exit_message(exitmsg):
    logger.critical("\033[91m{}\033[0m".format("Fatal Error: " + exitmsg))
    sys.exit(1)


# Function to check if the VT API key is valid
def check_VTAPIkey(VT_APIKey):
    # Google IP just for validating key
    ip = "8.8.8.8"
    url = "https://www.virustotal.com/api/v3/ip_addresses/" + ip
    payload = {}
    headers = {"x-apikey": VT_APIKey}
    response = requests.request("GET", url, headers=headers, data=payload).text
    data = json.loads(response)
    if "error" not in data:
        # Print pretty json response
        # print(json.dumps(data, indent=4, sort_keys=True))
        logger.info("Virus Total Key Validation: \033[92m{}\033[0m".format("Success"))
        return True
    else:
        error_message(json.dumps(data["error"], indent=4, sort_keys=True))
        exit_message("Virus Total Key Validation failed")
        return False
