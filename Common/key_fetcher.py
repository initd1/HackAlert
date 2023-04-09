import configparser
import os

from .utils import exit_message


def getVTAPIKey():
    config = configparser.ConfigParser()

    if config.read("Config/config.ini"):
        pass
    else:
        exit_message("Config file not found")
    try:
        VT_APIKey = config["APIKeys"]["VT_APIKey"]
    except Exception as err:
        exit_message(f"VT API Key not found in config file: {str(err)}")
        return
    if VT_APIKey == "":
        exit_message("VT API Key could not be retrieved")
        return
    else:
        return VT_APIKey


def getHIBPAPIKey(config_name="config.ini"):
    config = configparser.ConfigParser()

    if config.read(os.path.join("Config", config_name)):
        pass
    else:
        exit_message("Config file not found")
    try:
        HIBP_APIKey = config["APIKeys"]["HIBP_APIKey"]
    except Exception as err:
        exit_message(f"HIBP API Key not found in config file: {str(err)}")
        return  # Satisfies LSP despite redundancy.

    if HIBP_APIKey == "":
        exit_message("HIBP API Key could not be retrieved")
        return  # See above.
    else:
        return HIBP_APIKey
