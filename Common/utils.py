# Utils file to:
    # fetch the relevant API keys of different services
    # validate keys
    # process non critical and fatal errors
    # TODO: Logging to file
import requests
import json
import re
import ipaddress
from termcolor  import colored
import sys
import configparser
from . import utils

def error_message(errormsg):
    print(colored("Error: "+errormsg, 'red'))
    # TODO: Extend error module to log to error log file
    # print(errormsg)

def exit_message(exitmsg):
    print("\033[91m{}\033[0m".format("Fatal Error: "+exitmsg))
    exit()

class Validator:
    def is_valid_email(self, email):
         # Verify email format
         # TODO: Add a list of email domains accepted..may be
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            # print("Email address validation: \033[92m{}\033[0m".format("Success"))
            return True
        else:
            return False

    def is_valid_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError as err:
            return False
        
    # Function to check if the VT API key is valid
    def check_VTAPIkey(self, VT_APIKey):
        # Google IP just for validating key
        ip = "8.8.8.8"
        url = "https://www.virustotal.com/api/v3/ip_addresses/"+ip
        payload={}
        headers = {
        'x-apikey': VT_APIKey
        }
        response = requests.request("GET", url, headers=headers, data=payload).text
        data = json.loads(response)
        if 'error' not in data:
            # Print pretty json response
            # print(json.dumps(data, indent=4, sort_keys=True))
            print("Virus Total Key Validation: \033[92m{}\033[0m".format("Success"))
            return True
        else:
            error_message(json.dumps(data['error'], indent=4, sort_keys=True))
            exit_message("Virus Total Key Validation failed")
            return False

    # def check_VTAPIkey(self, VT_APIKey):
        # instead of wasting a call to HIBP API just to check validity of key, 
        # execute the call for the actual query and then throw error if key is 
        # invalid (since likelihood of key being wrong is slim)

class KeyFetcher:
    def getVTAPIKey(self):
        try:
            config = configparser.ConfigParser()
            config.read('Config/config.ini')
            # Get the Virus Total API key from the config file
            VT_APIKey = config['APIKeys']['VT_APIKey']
            return VT_APIKey
        except Exception as er:
            utils.error_message(er)

    def getHIBPAPIKey(self):
        try:
            config = configparser.ConfigParser()
            config.read('Config/config.ini')
            # Get the Virus Total API key from the config file
            HIBP_APIKey = config['APIKeys']['HIBP_APIKey']
            return HIBP_APIKey
        except Exception as er:
            utils.error_message(er)

    # def getOTXAPIKey(self):
    #     # Read the line in the file OTX_APIKey and store as a variable called OTX_APIKey
    #     try:
    #         OTX_APIKey = open('OTX_APIKey', 'r').readline().strip()
    #         print('OTX_APIKey: ' + OTX_APIKey)
    #         return OTX_APIKey
    #     except:
    #         print("Error reading OTX_APIKey file. Please check if the file exists and has the correct API key")
    #         exit()
