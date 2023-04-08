import ipaddress
import json
import logging
import re

import requests

from Common.utils import error_message, exit_message

logger = logging.getLogger("")


class Validator:
    """Checks integrity/format of ip addresses and emails"""

    @classmethod
    def is_valid_email(cls, email):
        """Verifies email format.

        :param email: UTF email format.
        """

        # TODO: Add a list of email domains accepted.. maybe.

        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"  # pyright: ignore

        return re.search(regex, email)

    def is_valid_ip(self, ip):
        """Verifies ip validity (ipv4?)"""

        try:
            ipaddress.ip_address(ip)
            return True
        except Exception:
            return False

    def is_valid_username(self, username):
        # Verify username format
        # TODO: Add a list of username domains accepted..may be
        if re.match(r"^[a-zA-Z0-9\-\_\!\@\#\$\%\^\&\*\(\)]+", username):
            # print("Input is a valid username")
            return True
        else:
            # print("Invalid username ")
            return False

    # Function to check if the VT API key is valid
    def check_VTAPIkey(self, VT_APIKey):
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
            logger.info(
                "Virus Total Key Validation: \033[92m{}\033[0m".format("Success")
            )
            return True
        else:
            error_message(json.dumps(data["error"], indent=4, sort_keys=True))
            exit_message("Virus Total Key Validation failed")
            return False
