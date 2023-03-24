from Common.utils import getVT_APIKey

# Script name: virus-total-api.py
# Description: Python script to find IPs with bad reputation by querying the Virus total API
# Input:
  # 1. New Line delimited file with IP addresses and placed in the same directory as this script
  # 2. Virus total API key
# Output
  # List of IPs with bad reputation and the score of each IP

import requests
import json
import time

# ENTER FILE NAME WITH IPS AND THE API KEY BELOW
#file = "badips.txt"
#APIKey = ''

# Function to give help menu to users
def help():
  print("Manual")
  print("=======")
  print("1. Enter the file name with the list of IPs in the same directory as this script")
  print("2. Enter the VirusTotal API key")
  print("3. Run the script")
  
# Function to get the file name from the user
def get_file():
  file = input("Enter the file name with the list of IPs: ")
  return file 

# Function to get the API key from the user
def get_apikey():
  apikey = input("Enter the VirusTotal API key: ")
  return apikey

# Function to get the user input
def get_input():
  file = get_file()
  apikey = get_apikey()
  return file, apikey

# Function to check if the file exists
def check_file(file):
  try:
    file = open(file)
    file.close()
    return True
  except:
    return False
  
# Function to check if the API key is valid
def check_apikey(apikey):
  # Google IP just for validating key
  ip = "8.8.8.8"
  url = "https://www.virustotal.com/api/v3/ip_addresses/"+ip
  payload={}
  headers = {
    'x-apikey': apikey
  }
  response = requests.request("GET", url, headers=headers, data=payload).text
  data = json.loads(response)
  print(data['error']['code'])
  if data['error']['code'] == "Forbidden":
    return False
  else:
    return True
  
# Function to check if the user input is valid
def check_input(file, apikey):
  if check_file(file) and check_apikey(apikey):
    return True
  else:
    return False

# Function to run the script
def run_script():
  file, apikey = get_input()
  # fail script if no input is given
  if not get_input():
    print("No input given")
    help()
    exit()
  if check_input(file, apikey):
    print("Running script")
    ip_list = []
    bad_ip_list = []
    file = open(file)
    for ip in file:
      ip = ip.strip("\n")
      ip_list.append(ip)
    file.close()
    
    # Due to API license limitation, only 4 IPs can be queries in a minute
    while len(ip_list) > 0:
      # Get IP list in groups of 4 IPs at a time
      ip_quad = ip_list[:4]

      # Send the IP quad to be queried by the API 
      response = queryIP(apikey, ip_quad, bad_ip_list)
      # Delete the processed IP quad
      del ip_list[:4]

      if len(ip_list) > 0:
        print("Sleeping 60 seconds due to API license limitation")
        time.sleep(60)
  else:
    print("Invalid input")
    help()

def queryIP(apikey, ip_quad, bad_ip_list):
  vt_api = apikey
  for ip in ip_quad:
    url = "https://www.virustotal.com/api/v3/ip_addresses/"+ip
    payload={}
    headers = {
      'x-apikey': vt_api
    }
    # catch error if below line fails
    # query api and get response. If query fails, catch the error and print the error
    try:
      response = requests.request("GET", url, headers=headers, data=payload).text

      data = json.loads(response)
      stats = data['data']['attributes']['last_analysis_stats']
      print("Results of IP ==>",ip,":", stats)
      if stats['malicious'] > 0 or stats['suspicious'] > 0 :
        bad_ip_list.append(ip)
      return bad_ip_list
    except:
      print("Error querying API")
      # print the error
      print(response)
      exit()

if __name__ == "__main__":

  # Run the script
  run_script()

  print("\n\n=============VirusTotal IP Reputation Results=============") 
  for bad_ip in bad_ip_list:
    print(bad_ip)
  print("\n")

  # # Unit test to check if the script is working as expected
  # def test():
  #   file = "badips.txt"
  #   apikey = "1234567890"
  #   if check_input(file, apikey):
  #     print("Test passed")
  #   else:
  #     print("Test failed")
  
  # # Run the unit test
  # test()

# create a sample file with IPs
# file = open("badips.txt", "w")
# file.write("12.