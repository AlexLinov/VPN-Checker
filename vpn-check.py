#!/usr/bin/python3

import openpyxl
import requests
import json
import pandas as pd
import subprocess

# Read input file and extract first IP address
ips = pd.read_csv('Location_of_IP_List', header=None)
ip = ips.iloc[0, 0]

block_list = []
company_list = []

# Loop through all IP addresses in the input file
for index, row in ips.iterrows():
    ip = row[0]
    response = requests.get(f"https://vpnapi.io/api/{ip}?key=YOUR_API_KEY")
    json = response.json()

    # Check if the IP is a VPN, proxy, Tor node, or relay and add to respective block lists
    if "security" in json:
        security = json["security"]
        if security.get("vpn") or security.get("proxy") or security.get("tor") or security.get("relay"):
            block_list.append(json["network"]["network"])
            company_list.append(json["network"]["autonomous_system_organization"])

# Write block lists to output files if they contain data
if block_list:
    pd.DataFrame(block_list).to_csv('WRITE_LOCATION_OF/block_list.txt', header=False, index=False)
if company_list:
    pd.DataFrame(company_list).to_csv('WRITE_LOCATION_OF/company_list.txt', header=False, index=False)
