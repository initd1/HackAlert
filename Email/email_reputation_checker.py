import requests
import json
from termcolor import colored
from Common import utils as utils
from Common.utils import KeyFetcher
from Common.breach_checker import BreachChecker

class EmailBreachChecker:
    def __init__(self, email):
        self.email = email

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
            print("Downloading full breach data from HIBP")
            breaches = json.loads(response)
            with open('all_breaches.json', 'w') as f:
                json.dump(breaches, f)
        except Exception as e:
            utils.error_message(e)

    # Function to check email for breaches from HIBP
    def checkEmailBreach(self, email):
        keyfetcher = KeyFetcher()
        hibp_key = keyfetcher.getHIBPAPIKey()
        url = "https://haveibeenpwned.com/api/v3/breachedaccount/"+email
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
            print(colored("No breaches found for this email","green"))
            exit()
        data = json.loads(response.text)
        # Validating the response during execution instead of wasting a call for validation
        if 'statusCode' not in data:
            print("Query successful")
            for breach_name in data:
            # print("Breach name: ", breach_name['Name'])
                with open('all_breaches.json', 'r')  as f:
                    search_name = breach_name['Name']
                    # print("Searching for breach name: ", search_name)
                    breaches = json.load(f) 
                    # print(breaches)
                    for breach in breaches:
                        if 'Name' in breach and breach['Name'] == search_name:
                            print("\n\n" + colored("Account name:", "blue"), colored(email, "red"))
                            if 'Name' in breach:
                                print(colored("Breach name:", "blue"), colored(breach_name['Name'], "red"))
                            if 'Description' in breach:
                                print(colored("Breach description:", "blue"), colored(breach['Description'], "red"))
                            if 'BreachDate' in breach:
                                print(colored("Breach date:", "blue"), colored(breach['BreachDate'], "white"))
                            if 'DataClasses' in breach:
                                print(colored("Data classes that were part of this breach:", "blue"), colored(breach['DataClasses'], "red"))
                            if 'IsSensitive' in breach and breach['IsSensitive'] == True:
                                print(colored("Breach is sensitive:", "blue"), colored(breach['IsSensitive'], "yellow"))
                            if 'IsSensitive' in breach and breach['IsSensitive'] == False:
                                print(colored("Breach is sensitive:", "blue"), colored(breach['IsSensitive'], "green"))
                            if 'IsVerified' in breach and breach['IsVerified'] == True:
                                print(colored("Breach is verified:", "blue"), colored(breach['IsVerified'], "green"))
                            if 'IsVerified' in breach  and breach['IsVerified'] == False:
                                print(colored("Breach is verified:", "blue"), colored(breach['IsVerified'], "red"))
                            # print(colored("Number of accounts compromised:", "blue"), colored(breach['PwnCount'], "white"))
                            print(colored("Number of accounts compromised:", "blue"), colored('{:,}'.format(breach['PwnCount']), "white"))
                        else:
                            pass
        else:
            utils.error_message(data['message'])
