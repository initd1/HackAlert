# Base/Super class for accepting user input which will be called by other subclasses from each module: Email, IP, etc.
import re
import ipaddress
from Config.config import configure_logging
import logging

configure_logging()

# import argparse
# import asyncio


class BreachChecker:
    def is_valid_email(self, email):
        """Verify through regex that a given email is valid.

        :param email: the email to verify
        :return: if the email is valid.
        :rtype: bool
        """

        # Verify email format
        # TODO: Add a list of email domains accepted..may be
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            logging.debug("Input is a valid email address.")
            return True
        else:
            # print("Invalid email address.")
            return False

    def is_valid_ip(self, ip):
        """Verify that a given IP is valid.

        :param ip: the address to verify
        :return: if the ip is valid.
        :rtype: bool
        """
        valid = True
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            valid = False
        return valid
