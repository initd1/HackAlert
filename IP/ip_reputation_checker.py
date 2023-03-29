from Common.utils import getVT_APIKey

import requests
import json
import time

class IPReputationChecker:
  def __init__(self):
    self.bad_ip_list = []

  # Check Virus Total IP reputation
  def checkIPReputationVT(self, ip_list):
    # Check IP reputation from Virus Total
    # https://www.virustotal.com/gui/ip-address/
    pass
  
  # Check Talos IP reputation
  def checkIPReputationTalos(self, ip_list):
    # Check IP reputation from Cisco Talos
    # https://talosintelligence.com/reputation_center/lookup?search=
    # User requests to check IP reputation from Cisco Talos
    print("Checking IP reputation from Cisco Talos")
    for ip in ip_list:
      url = "https://talosintelligence.com/reputation_center/lookup?search="+ip
      response = requests.request("GET", url).text
      if "This IP address has been observed to be associated with malicious activity." in response:
        print("IP: "+ip+" is malicious")
        self.bad_ip_list.append(ip)
      else:
        print("IP: "+ip+" is not malicious")
# Function to run the script
# def run_script():
#   file, apikey = get_input()
#   # fail script if no input is given
#   if not get_input():
#     print("No input given")
#     help()
#     exit()
#   if check_input(file, apikey):
#     print("Running script")
#     ip_list = []
#     bad_ip_list = []
#     file = open(file)
#     for ip in file:
#       ip = ip.strip("\n")
#       ip_list.append(ip)
#     file.close()
    
#     # Due to API license limitation, only 4 IPs can be queries in a minute
#     while len(ip_list) > 0:
#       # Get IP list in groups of 4 IPs at a time
#       ip_quad = ip_list[:4]

#       # Send the IP quad to be queried by the API 
#       response = queryIP(apikey, ip_quad, bad_ip_list)
#       # Delete the processed IP quad
#       del ip_list[:4]

#       if len(ip_list) > 0:
#         print("Sleeping 60 seconds due to API license limitation")
#         time.sleep(60)
#   else:
#     print("Invalid input")
#     help()

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

# if __name__ == "__main__":

  # Run the script
  # run_script()

  # print("\n\n=============VirusTotal IP Reputation Results=============") 
  # for bad_ip in bad_ip_list:
  #   print(bad_ip)
  # print("\n")

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