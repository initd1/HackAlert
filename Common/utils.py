# Utils file to:
    # fetch the relevant API keys of different services
    # validate keys
    # process non critical and fatal errors
    # TODO: Logging to file
import requests
import json
import re
import ipaddress

def help():
    print("Usage: python3 main.py --<artifact to check> <artifact>")
    print("Example: python3 main.py --email bill.g@gmail.com")
    print("Example: python3 main.py --ip 201.122.41.15")
    exit()

def error_message(errormsg):
    print("Error:", {errormsg})
    # help()

def exit_message(exitmsg):
    print(f"Fatal Error:", {exitmsg})
    exit()

class Validator:
    def is_valid_email(self, email):
         # Verify email format
         # TODO: Add a list of email domains accepted..may be
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Input is a valid email address.")
            return True
        else:
            # print("Invalid email address.")
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
        # Print json in a well formatted form
        # print(json.dumps(json.loads(response), indent=4, sort_keys=True))
        data = json.loads(response)
        # if data['error']['code'] == 'WrongCredentialsError':
        #     er = "Virus Total Key Validation:", data['error']['code']
        if data['error']['code']:
            error_message(data['error']['code'])
            return False
        else:
            return True


class KeyFetcher:
    def getVTAPIKey(self):
        # Read the line in the file VT_APIKey and store as a variable called VT_APIKey
        try:
            VT_APIKey = open('VT_APIKey', 'r').readline().strip()
            print('VT_APIKey: ' + VT_APIKey)
            return VT_APIKey
        except:
            # print("Error reading VT_APIKey file. Please check if the file exists and has the correct API key")
            exit_message("Error reading VT_APIKey file. Please check if the file exists and has the correct API key")
            # return False

    def getOTXAPIKey(self):
        # Read the line in the file OTX_APIKey and store as a variable called OTX_APIKey
        try:
            OTX_APIKey = open('OTX_APIKey', 'r').readline().strip()
            print('OTX_APIKey: ' + OTX_APIKey)
            return OTX_APIKey
        except:
            print("Error reading OTX_APIKey file. Please check if the file exists and has the correct API key")
            exit()

    def getHIBPAPIKey(self):
        try:
            HIBP_APIKey = open('HIBP_APIKey', 'r').readline().strip()
            print('HIBP_APIKey: ' + HIBP_APIKey)
            return HIBP_APIKey
        except:
            print("Error reading HIBP_APIKey file. Please check if the file exists and has the correct API key")
            exit()
