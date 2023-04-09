import json

import requests

from Common import key_fetcher
from Common.utils import *
from Common.validator import *


def checkIPReputationVT(ip_address):
    """Check Virus Total IP reputation.

    :param `ip_address`: IP address as a valid (non-local) ipv4 or ipv6 address.
    :type `ip`: str
    """
    virus_total_key = key_fetcher.getVTAPIKey()
    check_VTAPIkey(virus_total_key)

    print("Checking IP reputation from Virus Total for ip:", ip_address)
    url = "https://www.virustotal.com/api/v3/ip_addresses/" + ip_address
    payload = {}
    headers = {"x-apikey": virus_total_key}
    response = requests.request(
        "GET", url, headers=headers, data=payload  # pyright: ignore
    ).text
    data = json.loads(response)
    results = data["data"]["attributes"]["total_votes"]
    return results


def checkIPReputationTalos(ip_list):
    """Check IP reputation from Cisco Talos.

    URL: https://talosintelligence.com/reputation_center/lookup?search=
    User requests to check IP reputation from Cisco Talos
    """

    print("Checking IP reputation from Cisco Talos")
    for ip in ip_list:
        url = "https://talosintelligence.com/reputation_center/lookup?search=" + ip
        response = requests.request("GET", url).text
        if (
            "This IP address has been observed to be associated with malicious activity."
            in response
        ):
            print("IP: " + ip + " is malicious")
            # TODO dump to json file
            continue
        else:
            print("IP: " + ip + " is not malicious")
