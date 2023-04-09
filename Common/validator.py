"""Checks integrity/format of ip addresses and emails"""

import ipaddress
import logging
import re

logger = logging.getLogger("")


def is_valid_email(email):
    """Verifies email format, comparing it to existing email name conventions.

    :param email: UTF email format.
    :type email: str
    :return: If the email is valid or not.
    :rtype: bool
    """

    # TODO: Add a list of email domains accepted.. maybe.

    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"  # pyright: ignore

    return re.search(regex, email)


def is_valid_ip(ip):
    """Verifies ip validity by using a common networking library.

    :param `ip`: IP address as a valid (non-local) ipv4 or ipv6 address.
    :type `ip`: str
    :return: The validity of `ip` and if it matches a given syntax.
    Note that this does not validate that it exists, merely that it follows a format.
    :rtype: bool
    """

    ip_is_valid = True

    try:
        ipaddress.ip_address(ip)
    except Exception:
        ip_is_valid = False
    return ip_is_valid


def is_valid_username(user_name):
    """Validate `user_name` as an alpha-numeric string.

    :param `user_name`: Username to validate
    :type `user_name`: str
    :return: If the username is valid and is an alpha-numeric string (or not).
    :rtype: bool
    """

    # TODO: Add a list of username domains accepted
    return re.match(r"^[a-zA-Z0-9\-\_\!\@\#\$\%\^\&\*\(\)]+", user_name)
