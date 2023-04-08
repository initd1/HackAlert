import configparser
import sys

from .utils import error_message, exit_message


def getVTAPIKey():
    config = configparser.ConfigParser()

    if config.read("Config/config.ini"):
        pass
    else:
        exit_message("Config file not found")
    try:
        VT_APIKey = config["APIKeys"]["VT_APIKey"]
    except Exception as er:
        error_message(str(er))
        exit_message("VT API Key not found in config file")
        sys.exit(1)
    if VT_APIKey == "":
        exit_message("VT API Key could not be retrieved")
    else:
        return VT_APIKey

def getHIBPAPIKey():
    config = configparser.ConfigParser()
    if config.read("Config/config.ini"):
        # print("Reading config file...")
        pass
    else:
        exit_message("Config file not found")
    try:
        HIBP_APIKey = config["APIKeys"]["HIBP_APIKey"]
    except Exception as er:
        error_message(str(er))
        exit_message("HIBP API Key not found in config file")
        sys.exit(1)
    if HIBP_APIKey == "":
        exit_message("HIBP API Key could not be retrieved")
    else:
        return HIBP_APIKey
