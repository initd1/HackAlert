"""
This module has the capacity to:
  - fetch the relevant API keys of different services
  - validate keys
  - process non critical and fatal errors
  - TODO: Logging to file
"""

import logging
import configparser

logger = logging.getLogger("")


def error_message(errormsg):
    logger.error(errormsg)

def exit_message(exitmsg):
    logger.critical("\033[91m{}\033[0m".format("Fatal Error: " + exitmsg))
    exit()



class KeyFetcher:
    @classmethod
    def getVTAPIKey(cls):
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
        if VT_APIKey == "":
            exit_message("VT API Key could not be retrieved")
        else:
            return VT_APIKey

    @classmethod
    def getHIBPAPIKey(cls):
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
        if HIBP_APIKey == "":
            exit_message("HIBP API Key could not be retrieved")
        else:
            return HIBP_APIKey
