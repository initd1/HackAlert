# Base/Super class for accepting user input which will be called by other subclasses from each module: Email, IP, etc.
from . import utils
import re
import ipaddress
# import argparse
# import asyncio
class BreachChecker:
    def is_valid_email(self, email):
         # Verify email format
         # TODO: Add a list of email domains accepted..may be
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Input is a valid email address.")
            return True
        else:
            # print("Invalid email address.")
            return False

    def is_valid_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError as err:
            return False