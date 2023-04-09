import json
import logging
import sys

import requests
from termcolor import colored

from Common import utils as utils
from Common.key_fetcher import *

logger = logging.getLogger("")


def periodicBreachDownloader():
    """Method to periodically download full breach data from HIBP so it can be
    used to lookup further details of a breach when an IP/Email is found in the breach data.
    """

    hibp_key = getHIBPAPIKey()
    url = "https://haveibeenpwned.com/api/v3/breaches"
    payload = {}
    headers = {
        "hibp-api-key": hibp_key,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Content-Type": "application/json",
    }
    try:
        response = requests.get(url, headers=headers, data=payload).text
        print("Downloading full breach data from HIBP")
        breaches = json.loads(response)
        with open("all_breaches.json", "w") as f:
            json.dump(breaches, f)
    except Exception as e:
        utils.error_message(str(e))


def checkUsernameBreach(username):
    """check username for breaches from HIBP

    :param username: Username to check breaches for.
    :type username: str
    """

    hibp_key = getHIBPAPIKey()
    url = "https://haveibeenpwned.com/api/v3/breachedaccount/" + username
    payload = {}
    headers = {
        "hibp-api-key": hibp_key,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Content-Type": "application/json",
    }
    try:
        response = requests.get(url, headers=headers, data=payload)
    except Exception as e:
        utils.error_message(str(e))
        sys.exit(1)
    if response.status_code == 404:
        logger.info("No breaches found for this username")
        exit()
    data = json.loads(response.text)

    # Validate response during execution - prevents wasting call
    if "statusCode" not in data:
        for breach_name in data:
            with open("all_breaches.json", "r") as f:
                search_name = breach_name["Name"]
                breaches = json.load(f)
                for breach in breaches:
                    if "Name" in breach and breach["Name"] == search_name:
                        print(
                            "\n\n" + colored("Account name:", "blue"),
                            colored(username, "red"),
                        )
                        if "Name" in breach:
                            print(
                                colored("Breach name:", "blue"),
                                colored(breach_name["Name"], "red"),
                            )
                        if "Description" in breach:
                            print(
                                colored("Breach description:", "blue"),
                                colored(breach["Description"], "red"),
                            )
                        if "BreachDate" in breach:
                            print(
                                colored("Breach date:", "blue"),
                                colored(breach["BreachDate"], "white"),
                            )
                        if "DataClasses" in breach:
                            print(
                                colored(
                                    "Data classes that were part of this breach:",
                                    "blue",
                                ),
                                colored(breach["DataClasses"], "red"),
                            )
                        if "IsSensitive" in breach:
                            if breach["IsSensitive"]:
                                print(
                                    colored("Breach is sensitive:", "blue"),
                                    colored(breach["IsSensitive"], "yellow"),
                                )
                            else:
                                print(
                                    colored("Breach is sensitive:", "blue"),
                                    colored(breach["IsSensitive"], "green"),
                                )
                        if "IsVerified" in breach:
                            if breach["IsVerified"]:
                                print(
                                    colored("Breach is verified:", "blue"),
                                    colored(breach["IsVerified"], "green"),
                                )
                            else:
                                print(
                                    colored("Breach is verified:", "blue"),
                                    colored(breach["IsVerified"], "red"),
                            )
                        print(
                            colored("Number of accounts compromised:", "blue"),
                            colored(breach["PwnCount"], "white"),
                        )
                    else:
                        pass
    else:
        utils.error_message(data["message"])
