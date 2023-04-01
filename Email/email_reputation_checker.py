import requests
import json
from termcolor import colored
from Common import utils as utils
from Common.utils import KeyFetcher
from Common.breach_checker import BreachChecker


# EmailReputationChecker class inherits methods from BreachChecker super class
class EmailBreachChecker:
    def __init__(self, email):
        self.email = email

    # Function to periodically download full breach data from HIBP so it can be 
    # used to lookup further details of a breach when an IP/Email is found in the breach data
    def periodicBreachDownloader(self):
        keyfetcher = KeyFetcher()
        hibp_key = keyfetcher.getHIBPAPIKey()
        # print('HIBPKEY in EmailBreachChecker: ', hibp_key)
        url = "https://haveibeenpwned.com/api/v3/breaches"
        payload={}
        headers = {
        'hibp-api-key': hibp_key,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Content-Type': 'application/json'
        }
        try:
            response = requests.get(url, headers=headers, data=payload).text
            print(colored("Downloading full breach data from HIBP ...","grey"))
            # print("Response: ", response)
            breaches = json.loads(response)
            with open('all_breaches.json', 'w') as f:
                json.dump(breaches, f)
        except Exception as e:
            utils.error_message("Downloading all breaches failed",e)

    # Function to check email for breaches from HIBP
    def checkEmailBreach(self, email):
        # Create instance of KeyFetcher class
        keyfetcher = KeyFetcher()
        # Get HIBP API key from KeyFetcher class
        hibp_key = keyfetcher.getHIBPAPIKey()
        # Code to check Email reputation from HIBP
        # print("Checking Email breach from HIBP for email:", email)
        # Check Email breach from HIBP
        url = "https://haveibeenpwned.com/api/v3/breachedaccount/"+email
        payload={}
        headers = {
        'hibp-api-key': hibp_key,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Content-Type': 'application/json'
        }
        try:
            response = requests.get(url, headers=headers, data=payload).text
            data = json.loads(response)
        except requests.exceptions.RequestException as e:
            utils.error_message(e)
            # sys.exit(1)
        # pretty print full json response
        # print(json.dumps(data, indent=4, sort_keys=True))
        # Loop through each breach name
        for breach_name in data:
            # print("Breach name: ", breach_name['Name'])
            # Open all breaches file
            with open('all_breaches.json', 'r')  as f:
                search_name = breach_name['Name']
                # print("Searching for breach name: ", search_name)
                # Load all breaches into a variable
                breaches = json.load(f) 
                # print(breaches)
                # Loop through each breach
                for breach in breaches:
                    # If breach name matches search name then print details about breach
                    if breach['Name'] == search_name:
                        print("\n\n" + colored("Account name:", "blue"), colored(email, "red"))
                        print(colored("Breach name:", "blue"), colored(breach_name['Name'], "red"))
                        print(colored("Breach description:", "blue"), colored(breach['Description'], "red"))
                        print(colored("Data classes that were part of this breach:", "blue"), colored(breach['DataClasses'], "red"))
                        print(colored("Breach date:", "blue"), colored(breach['BreachDate'], "white"))
                        if breach['isVerified'] == True:
                            print(colored("Breach is verified:", "blue"), colored(breach['IsVerified'], "green"))
                        else:
                            print(colored("Breach is verified:", "blue"), colored(breach['IsVerified'], "red"))
                        print(colored("Number of accounts compromised:", "blue"), colored(breach['PwnCount'], "white"))
    # return data