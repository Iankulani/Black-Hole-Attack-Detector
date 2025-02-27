# -*- coding: utf-8 -*-
"""
Created on Tue Feb  27 08:345:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("Black Hole Attack Detector")
print(Fore.GREEN+font)

import os
import subprocess
import re

def ping_ip(ip_address):
    """
    Ping the provided IP address to check if it is reachable.
    """
    # Run the ping command (using 1 packet for a quick test)
    try:
        # Windows uses "ping -n" and Linux uses "ping -c"
        # Adjust for the system's operating system (ping count of 1)
        if os.name == 'nt':  # For Windows
            response = subprocess.run(["ping", "-n", "1", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:  # For Linux or MacOS
            response = subprocess.run(["ping", "-c", "1", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Check if the ping was successful (no packet loss)
        if response.returncode == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error pinging IP: {e}")
        return False

def check_blackhole(ip_address):
    """
    Check if an IP address is potentially associated with a blackhole attack.
    A simple heuristic is to ping the address and see if it's unreachable.
    """
    print(f"Checking IP address: {ip_address}")

    # Attempt to ping the IP address
    reachable = ping_ip(ip_address)

    if not reachable:
        print(f"IP address {ip_address} is not reachable. This could indicate a blackhole attack or routing issues.")
        # Further actions could include:
        # - Performing traceroutes to check the routing path.
        # - Checking for known blackhole IPs using external APIs or databases.
        # For now, we print a basic warning.
        return True
    else:
        print(f"IP address {ip_address} is reachable. No blackhole detected.")
        return False

def main():
    
    print("This tool checks if an IP address may be associated with a Blackhole or Sinkhole attack.")

    while True:
        # Prompt user to input an IP address
        ip_address = input("Enter the IP address to check ('exit' to quit):").strip()

        if ip_address.lower() == 'exit':
            print("Exiting the tool. Thank you for using this Tool Goodbye!")
            break

        # Validate IP address format
        if validate_ip(ip_address):
            print(f"Validating IP address: {ip_address}")
            if check_blackhole(ip_address):
                print(f"Warning: IP address {ip_address} may be associated with a Blackhole attack!")
            else:
                print(f"IP address {ip_address} is likely safe.")
        else:
            print(f"Invalid IP address format: {ip_address}. Please try again.")

def validate_ip(ip_address):
    """
    Validates the IP address format.
    Checks if the IP address is in the form of 'xxx.xxx.xxx.xxx'
    where each 'xxx' is a number between 0 and 255.
    """
    pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    if re.match(pattern, ip_address):
        return True
    return False

if __name__ == "__main__":
    main()
