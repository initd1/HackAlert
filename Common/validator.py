"""Checks integrity/format of ip addresses and emails"""

import ipaddress
import logging
import re

from Common.utils import error_message, exit_message

logger = logging.getLogger("")


def is_valid_email(email):
    """Verifies email format.

    :param email: UTF email format.
    """

    # TODO: Add a list of email domains accepted.. maybe.

    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"  # pyright: ignore

    return re.search(regex, email)


def is_valid_ip(ip):
    """Verifies ip validity (ipv4?)"""

    try:
        ipaddress.ip_address(ip)
        return True
    except Exception:
        return False


def is_valid_username(username):
    # Verify username format
    # TODO: Add a list of username domains accepted..may be
    if re.match(r"^[a-zA-Z0-9\-\_\!\@\#\$\%\^\&\*\(\)]+", username):
        # print("Input is a valid username")
        return True
    else:
        # print("Invalid username ")
        return False
