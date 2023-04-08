import json

import requests

from Common import utils as utils
from Common.utils import KeyFetcher
from Common.utils import Validator

# IPReputationChecker class inherits methods from BreachChecker super class
class IPReputationChecker:
    def __init__(self, ip_address):
        self.ip_address = ip_address

  # Check Virus Total IP reputation
    def checkIPReputationVT(self, ip_address):
        keyfetch_vt = KeyFetcher()
        vtkey = keyfetch_vt.getVTAPIKey()
        validator = Validator()
        validator.check_VTAPIkey(vtkey)

        print("Checking IP reputation from Virus Total for ip:", ip_address)
        # Check IP reputation from Virus Total
        url = "https://www.virustotal.com/api/v3/ip_addresses/"+ip_address
        payload={}
        headers = {
                'x-apikey': vtkey
                }
        response = requests.request("GET", url, headers=headers, data=payload).text  # pyright: ignore
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
        print("Checking IP reputation from Cisco Talos")
        for ip in ip_list:
            url = "https://talosintelligence.com/reputation_center/lookup?search="+ip
            response = requests.request("GET", url).text
            if "This IP address has been observed to be associated with malicious activity." in response:
                print("IP: "+ip+" is malicious")
                self.bad_ip_list.append(ip)
            else:
                print("IP: "+ip+" is not malicious")
