"""
Description: Base/Super class for accepting user input which will be called by other subclasses
             from each module: Email, IP, etc.
"""

import re
import ipaddress


class BreachChecker:

    @classmethod
    def is_valid_email(cls, email) :
        """ Verifies email format """

         # TODO: Add a list of email domains accepted..may be

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
        return re.search(regex,email)

    @classmethod
    def is_valid_ip(cls, ip):

        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False
