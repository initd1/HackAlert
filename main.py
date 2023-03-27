
import requests
import json
import argparse
from Common.utils import Validator
from IP.ip_reputation_checker import IPReputationChecker
from Common import utils

def accept_user_input():
    # Instantiate the Validator class
    validator = Validator()

    # Accept user input
    try:
        parser = argparse.ArgumentParser(description="Check if the given data has been compromised in a data breach.")
        parser.add_argument("-e", "--email", help="Email address to check")
        parser.add_argument("-i", "--ip", help="IP address to check")
        args = parser.parse_args()
    except Exception as er:
        # print(er)
        utils.error_message(er)
    if args.email:
        # if valid email, print and return email
        if validator.is_valid_email(args.email) == True:
            print(args.email)
            # Call the email module to check if the email is in a breach
            # return args.email
        else:
            utils.error_message("Invalid email address")
    elif args.ip:
        # if valid IP, print and return IP
        if validator.is_valid_ip(args.ip) == True:
            print(args.ip)
            # Call the IP module to check if the IP is in a breach
            ip_checker = IPReputationChecker(args.ip)
            vtip_results = ip_checker.checkIPReputationVT(args.ip)   
            # return args.ip
        else:
            utils.error_message("Invalid IP address")
    else:
        utils.error_message("Invalid input received.")

if __name__ == '__main__':
    accept_user_input()
    

