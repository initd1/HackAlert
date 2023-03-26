# Utils file to fetch the relevant API keys of different services
import requests
import json

def getVT_APIKey():
    # Read the line in the file VT_APIKey and store as a variable called VT_APIKey
    try:
        VT_APIKey = open('VT_APIKey', 'r').readline().strip()
        print('VT_APIKey: ' + VT_APIKey)
        return VT_APIKey
    except:
        print("Error reading VT_APIKey file. Please check if the file exists and has the correct API key")
        exit()

def getOTX_APIKey():
    # Read the line in the file OTX_APIKey and store as a variable called OTX_APIKey
    try:
        OTX_APIKey = open('OTX_APIKey', 'r').readline().strip()
        print('OTX_APIKey: ' + OTX_APIKey)
        return OTX_APIKey
    except:
        print("Error reading OTX_APIKey file. Please check if the file exists and has the correct API key")
        exit()

def getHIBP_APIKey():
   try:
        HIBP_APIKey = open('HIBP_APIKey', 'r').readline().strip()
        print('HIBP_APIKey: ' + HIBP_APIKey)
        return HIBP_APIKey
    except:
        print("Error reading HIBP_APIKey file. Please check if the file exists and has the correct API key")
        exit()

# Function to check if the user input is valid
# def check_input(file, apikey):
#   if check_file(file) and check_VTapikey(apikey):
#     return True
#   else:
#     return False

# Function to check if the API key is valid
def check_VTapikey(VT_APIKey):
    # Google IP just for validating key
    ip = "8.8.8.8"
    url = "https://www.virustotal.com/api/v3/ip_addresses/"+ip
    payload={}
    headers = {
    'x-apikey': VT_APIKey
    }
    response = requests.request("GET", url, headers=headers, data=payload).text
    # Print json in a well formatted form
    print(json.dumps(json.loads(response), indent=4, sort_keys=True))
    data = json.loads(response)
    print(data['error']['code'])
    if data['error']['code'] == "Forbidden":
        return False
    else:
        return True