import re
import ipaddress
import argparse
# import asyncio
from . import utils 

# Base class for accepting user input which will be called by other subclasses from each module: Email, IP, etc.
class BreachChecker:

	def __init__(self):
		pass

	def accept_user_input(self):
		# Code using argparse to accept user input
		parser = argparse.ArgumentParser(description="Check if an email address or IP address has been compromised in a data breach.")
		parser.add_argument("-e", "--email", help="Email address to check")
		parser.add_argument("-i", "--ip", help="IP address to check")
		args = parser.parse_args()
		# print email argument

	def is_valid_email(self, email):
		 # Verify email format
		if re.match(r"[^@]+@[^@]+\.[^@]+", email):
			print("Input is a valid email address.")
			return True
		else:
			print("Invalid email address.")
			return False

	def is_valid_ip(self, ip):
		try:
			ipaddress.ip_address(ip)
			return True
		except ValueError:
			return False

		# # Verify email format
		# if is_valid_email(args.email) == True:
		#     return input_value
		
		# # Verify IP address format
		# elif is_valid_ip(args.ip) == False:
		#     return input_value
		
		# else:
		#     print("Invalid input.")
		#     return None 
	

	

