# import requests
import argparse
import logging
import os
import sys

from termcolor import colored

from Common import utils
from Common.validator import Validator
from Email.email_reputation_checker import *
from IP.ip_reputation_checker import IPReputationChecker
from Username.username_reputation_checker import usernameBreachChecker


# Some basic colors for ✨
LOG_FORMAT = (
    "\033[1m%(asctime)s\033[0m \033[%(levelname)sm%(levelname)s\033[0m %(message)s"
)

logging.basicConfig(format=LOG_FORMAT, stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure the root logger to log to console
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logging.getLogger("").addHandler(console_handler)

# Add a FileHandler to write logs to file
file_handler = logging.FileHandler(os.path.join("Logs", "debug.log"))
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logging.getLogger("").addHandler(file_handler)


def accept_user_input():
    # Instantiate the Validator class
    validator = Validator()

    # Accept user input
    try:
        parser = argparse.ArgumentParser(
            description="Check if the given data has been compromised in a data breach."
        )
        parser.add_argument("-e", "--email", help="Email address to check")
        parser.add_argument("-i", "--ip", help="IP address to check")
        parser.add_argument("-u", "--username", help="Username to check")
        args = parser.parse_args()
    except Exception as er:
        # print(er)
        utils.error_message(er)
        sys.exit(1)

    # TODO: #9 Find a way to invoke each module in parallel if they are provided:
    # Example: python3 main.py -e asd@d.com -i 1.1.1.1
    # It would have to call email and IP modules and serve the results from each module

    if args.email:
        email_is_valid = Validator.is_valid_email(args.email)

        if email_is_valid:
            # print(args.email)
            # Call the email module to check if the email is in a breach
            print("Email Validation : \033[92m{}\033[0m".format("Success"))
            # Instantiate IPReputationChecker class
            periodicBreachDownloader()
            # breach_results = breach_checker.checkEmailBreach(args.email)
            # print("Email breach checker module results:", breach_results)
            # return args.email
        else:
            utils.exit_message("Invalid email address")
    elif args.ip:
        # if valid IP, print and return IP
        if validator.is_valid_ip(args.ip) == True:
            print("IP Validation : \033[92m{}\033[0m".format("Success"))
            # Instantiate IPReputationChecker class
            ip_checker = IPReputationChecker(args.ip)

            # Invoke VT IP Checker module
            vtip_results = ip_checker.checkIPReputationVT(args.ip)
            print("Virus Total results: ", vtip_results)

            # Invoke OTX IP Checker module
            # otx_results = ...
            # print("OTX results:",otx_results)
        else:
            utils.error_message("Invalid IP address")
    elif args.username:
        if validator.is_valid_username(args.username) == True:
            # print(args.username)
            # Call the username module to check if the username is in a breach
            print(colored("Username Validation:", "grey"), colored("Success", "green"))

            # Instantiate IPReputationChecker class
            breach_checker = usernameBreachChecker(args.ip)
            breach_checker.periodicBreachDownloader()
            # breach_results = breach_checker.checkUsernameBreach(args.username)
            # print("username breach checker module results:", breach_results)
            # return args.username
        else:
            utils.exit_message("Invalid username")
    else:
        utils.error_message("Invalid input received.")


if __name__ == "__main__":
    accept_user_input()
