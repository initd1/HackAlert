import sys
import json
import logging
import logging.config
from Common import utils as utils
from Common.utils import KeyFetcher
from Common.utils import Validator
from Common.breach_checker import BreachChecker
from Config.config import configure_logging
from termcolor import colored
import requests
from Common import utils

configure_logging()


class IPReputationChecker:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def checkIPReputationVT(self, ip_address):
        """This is a method that checks IP reputation from Virus Total

        Args:
            ip_address (IP): _description_

        Returns:
            _null_: No return value
        """
        keyfetch_vt = KeyFetcher()
        vtkey: str = keyfetch_vt.getVTAPIKey()  # pyright: ignore
        validator = Validator()
        validator.check_VTAPIkey(vtkey)
        logging.info(
            "{}{}".format(
                colored("Checking IP reputation from Virus Total for ip: ", "blue"),
                colored(ip_address, "red"),
            )
        )
        url = "https://www.virustotal.com/api/v3/ip_addresses/" + ip_address
        payload = {}
        headers: dict[str, str] = {"x-apikey": vtkey}
        response = requests.request("GET", url, headers=headers, data=payload).text
        data = json.loads(response)
        print(
            json.dumps(
                data["data"]["attributes"]["total_votes"], indent=4, sort_keys=True
            )
        )
        results = data["data"]["attributes"]["total_votes"]
        return results
