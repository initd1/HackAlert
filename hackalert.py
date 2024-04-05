import argparse
import logging
import logging.config
import sys

# from colorama import init
from termcolor import colored
from Common import utils
from Common.utils import Validator
from Config.config import configure_logging
from Email.email_reputation_checker import EmailBreachChecker
from IP.ip_reputation_checker import IPReputationChecker
from Username.username_reputation_checker import usernameBreachChecker
import logger


configure_logging()


def accept_user_input():
    """Handle command line input and match output accordingly."""

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
        utils.error_message(er)
        return

    # TODO: #9 Find a way to invoke each module in parallel if they are provided:
    # Example: python3 main.py -e asd@d.com -i 1.1.1.1
    # It would have to call email and IP modules and serve the results from each module

    if args.email:
        if validator.is_valid_email(args.email) == True:
            # print(args.email)
            # Call the email module to check if the email is in a breach
            logging.info("Email Validation : \033[92m{}\033[0m".format("Success"))
            # Instantiate IPReputationChecker class
            breach_checker = EmailBreachChecker(args.email)
            breach_checker.periodicBreachDownloader()
            breach_checker.checkEmailBreach(args.email)
            # print("Email breach checker module results:", breach_results)
            # return args.email
        else:
            utils.exit_message("Invalid email address")
            return
    elif args.ip:
        # if valid IP, print and return IP
        if validator.is_valid_ip(args.ip) == True:
            logging.info("IP Validation : \033[92m{}\033[0m".format("Success"))
            # Instantiate IPReputationChecker class
            ip_checker = IPReputationChecker(args.ip)

            # Invoke VT IP Checker module
            vtip_results = ip_checker.checkIPReputationVT(args.ip)
            # logging.info("Virus Total results: ", vtip_results)

            # Invoke OTX IP Checker module
            # otx_results = ...
            # print("OTX results:",otx_results)
        else:
            logging.error("Invalid IP address")
            return
    elif args.username:
        if validator.is_valid_username(args.username) == True:
            # print(args.username)
            # Call the username module to check if the username is in a breach
            logging.info(
                "{} {}".format(
                    colored("Username Validation:", "grey"), colored("Success", "green")
                )
            )

            # Instantiate IPReputationChecker class
            breach_checker = usernameBreachChecker(args.username)
            breach_checker.periodicBreachDownloader()
            breach_checker.checkUsernameBreach(args.username)
            # print("username breach checker module results:", breach_results)
            # return args.username
        else:
            logging.critical("Invalid username")
            sys.exit()
    else:
        logging.warning("Invalid input received.")


if __name__ == "__main__":
    accept_user_input()
