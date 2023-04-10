import logging
from Common import utils as utils
from Common.utils import KeyFetcher
from Common.utils import Validator
import requests
import json
from Config.config import configure_logging

configure_logging()

# IPReputationChecker class inherits methods from BreachChecker super class
class IPReputationChecker:
    def __init__(self, ip_address):
        self.ip_address = ip_address

  # Check Virus Total IP reputation
    def checkIPReputationVT(self, ip_address):
        keyfetch_vt = KeyFetcher()
        vtkey: str = keyfetch_vt.getVTAPIKey()  # pyright: ignore
        validator = Validator()
        validator.check_VTAPIkey(vtkey)

        logging.info("Checking IP reputation from Virus Total for ip:", ip_address)
        # Check IP reputation from Virus Total
        url = "https://www.virustotal.com/api/v3/ip_addresses/"+ip_address
        payload={}
        headers: dict[str, str] = {
        'x-apikey': vtkey
        }
        response = requests.request("GET", url, headers=headers, data=payload).text
        data = json.loads(response)
        # pretty print full json response
        # print(json.dumps(data, indent=4, sort_keys=True))
        results=data['data']['attributes']['total_votes']
        return results

    # Check Talos IP reputation
    def checkIPReputationTalos(self, ip_list):
        # Check IP reputation from Cisco Talos
        # https://talosintelligence.com/reputation_center/lookup?search=
        # User requests to check IP reputation from Cisco Talos
        logging.info("Checking IP reputation from Cisco Talos")
        for ip in ip_list:
            url = "https://talosintelligence.com/reputation_center/lookup?search="+ip
            response = requests.request("GET", url).text
            if "This IP address has been observed to be associated with malicious activity." in response:
                logging.info("IP: "+ip+" is malicious")
                # self.bad_ip_list.append(ip)
            else:
                logging.info("IP: "+ip+" is not malicious")

# # ==================
#     def queryIP(apikey, ip_quad, bad_ip_list):
#         vt_api = apikey
#         for ip in ip_quad:
#             url = "https://www.virustotal.com/api/v3/ip_addresses/"+ip
#             payload={}
#             headers = {
#             'x-apikey': vt_api
#             }
#             # catch error if below line fails
#             # query api and get response. If query fails, catch the error and print the error
#         try:
#             response = requests.request("GET", url, headers=headers, data=payload).text

#             data = json.loads(response)
#             stats = data['data']['attributes']['last_analysis_stats']
#             print("Results of IP ==>",ip,":", stats)
#             if stats['malicious'] > 0 or stats['suspicious'] > 0 :
#                 bad_ip_list.append(ip)
#             return bad_ip_list
#         except:
#             print("Error querying API")
#             print(response)
#             exit()
