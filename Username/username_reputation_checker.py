import json
import logging

import requests
from termcolor import colored

from Common import utils as utils
from Common.breach_checker import BreachChecker
from Common.utils import KeyFetcher
from Config.config import configure_logging

configure_logging()

# usernameReputationChecker class inherits methods from BreachChecker super class
class usernameBreachChecker:
    def __init__(self, username):
        self.username = username

    # Method to periodically download full breach data from HIBP so it can be 
    # used to lookup further details of a breach when an IP/Email is found in the breach data
    def periodicBreachDownloader(self):
        keyfetcher = KeyFetcher()
        hibp_key = keyfetcher.getHIBPAPIKey()
        url = "https://haveibeenpwned.com/api/v3/breaches"
        payload={}
        headers = {
        'hibp-api-key': hibp_key,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Content-Type': 'application/json'
        }
        try:
            response = requests.get(url, headers=headers, data=payload).text
            logging.info("Downloading full breach data from HIBP")
            breaches = json.loads(response)
            with open('all_breaches.json', 'w') as f:
                json.dump(breaches, f)
        except Exception as e:
            utils.error_message(str(e))

    # Function to check username for breaches from HIBP
    def checkUsernameBreach(self, username):
        keyfetcher = KeyFetcher()
        hibp_key = keyfetcher.getHIBPAPIKey()
        url = "https://haveibeenpwned.com/api/v3/breachedaccount/"+username
        payload={}
        headers = {
        'hibp-api-key': hibp_key,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Content-Type': 'application/json'
        }
        try:
            response = requests.get(url, headers=headers, data=payload)
        except Exception as e:
            utils.error_message(e.text)
        if response.status_code == 404:
            logging.info(colored("No breaches found for this username","green"))
            exit()
        data = json.loads(response.text)
        # Validating the response during execution instead of wasting a call for validation
        if 'statusCode' not in data:
            # print("Query successful")
            for breach_name in data:
            # print("Breach name: ", breach_name['Name'])
                with open('all_breaches.json', 'r')  as f:
                    search_name = breach_name['Name']
                    # print("Searching for breach name: ", search_name)
                    breaches = json.load(f) 
                    # print(breaches)
                    for breach in breaches:
                        if 'Name' in breach and breach['Name'] == search_name:
                            logging.info("\n\n" + colored("Account name:", "blue"), colored(username, "red"))
                            if 'Name' in breach:
                                logging.info(colored("Breach name:", "blue"), colored(breach_name['Name'], "red"))
                            if 'Description' in breach:
                                logging.info(colored("Breach description:", "blue"), colored(breach['Description'], "red"))
                            if 'BreachDate' in breach:
                                logging.info(colored("Breach date:", "blue"), colored(breach['BreachDate'], "white"))
                            if 'DataClasses' in breach:
                                logging.info(colored("Data classes that were part of this breach:", "blue"), colored(breach['DataClasses'], "red"))
                            if 'IsSensitive' in breach and breach['IsSensitive'] == True:
                                logging.info(colored("Breach is sensitive:", "blue"), colored(breach['IsSensitive'], "yellow"))
                            if 'IsSensitive' in breach and breach['IsSensitive'] == False:
                                logging.info(colored("Breach is sensitive:", "blue"), colored(breach['IsSensitive'], "green"))
                            if 'IsVerified' in breach and breach['IsVerified'] == True:
                                logging.info(colored("Breach is verified:", "blue"), colored(breach['IsVerified'], "green"))
                            if 'IsVerified' in breach  and breach['IsVerified'] == False:
                                logging.info(colored("Breach is verified:", "blue"), colored(breach['IsVerified'], "red"))
                            logging.info(colored("Number of accounts compromised:", "blue"), colored(breach['PwnCount'], "white"))
                        else:
                            pass
        else:
            utils.error_message(data['message'])
