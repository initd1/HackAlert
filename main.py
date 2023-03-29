
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
    
    # TODO: Find a way to invoke each module in parallel if they are provided:
    # Example: python3 main.py -e asd@d.com -i 1.1.1.1
    # It would have to call email and IP modules and serve the results from each module

    if args.email:
        if validator.is_valid_email(args.email) == True:
            print(args.email)
            # Call the email module to check if the email is in a breach
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
    else:
        utils.error_message("Invalid input received.")

if __name__ == '__main__':
    accept_user_input()