
import requests
import json
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


