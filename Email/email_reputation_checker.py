import requests
import json
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
            print("Downloading full breach data from HIBP")
            # print("Response: ", response)
            breaches = json.loads(response)
            with open('all_breaches.json', 'w') as f:
                json.dump(breaches, f)
        except Exception as e:
            utils.error_message("Downloading all breaches failed",e)

    # Function to check email for breaches from HIBP
    def checkEmailBreach(self, email):
        keyfetcher = KeyFetcher()
        hibp_key = keyfetcher.getHIBPAPIKey()
        # Code to check Email reputation from HIBP
        print("Checking Email breach from HIBP for email:", email)
        # Check Email breach from HIBP
        url = "https://haveibeenpwned.com/api/v3/breachedaccount/"+email
        payload={}
        headers = {
        'hibp-api-key': hibp_key,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers, data=payload).text
        data = json.loads(response)
        # pretty print full json response
        # print(json.dumps(data, indent=4, sort_keys=True))
        for breach_name in data:
            # print("Breach name: ", breach_name['Name'])
            with open('all_breaches.json', 'r')  as f:
                search_name = breach_name['Name']
                print("Searching for breach name: ", search_name)
                breaches = json.load(f) 
                # print(breaches)
                for breach in breaches:
                    if breach['Name'] == search_name:
                        print("\n\nAccount name:", email)
                        print("Breach name: ", breach_name['Name'])
                        print("Breach description: ", breach['Description'])
                        print("Data classes that were part of this breach: ", breach['DataClasses'])
                        print("Breach date: ", breach['BreachDate'])
                        print("Breach is verified: ", breach['IsVerified'])
                        print("Number of accounts compromised: ", breach['PwnCount'])
    # return data