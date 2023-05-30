#!/usr/bin/python3

import openpyxl
import requests
import json
import pandas as pd
import subprocess
import sys
from tqdm import tqdm
import time

# Read input file and extract first IP address
if len(sys.argv) != 2:
    print("Usage: python script.py <input_file_location>")
    sys.exit(1)

# Read input file and extract first IP address
ips = pd.read_csv(sys.argv[1], header=None)
ip = ips.iloc[0, 0]

block_list = []
company_list = []

total_ips = len(ips)
progress_bar = tqdm(total=total_ips, unit="IP")

# Loop through all IP addresses in the input file
for index, row in ips.iterrows():
    ip = row[0]
    response = requests.get(f"https://vpnapi.io/api/{ip}?key=API_KEY")
    json_data = response.json()

    # Check if the IP is a VPN, proxy, Tor node, or relay and add to respective block lists
    if "security" in json_data:
        security = json_data["security"]
        if security.get("vpn") or security.get("proxy") or security.get("tor") or security.get("relay"):
            block_list.append(json_data["network"]["network"])
            company_name = json_data["network"]["autonomous_system_organization"]
            if "MICROSOFT" not in company_name and "FUSE" not in company_name:
                company_list.append(company_name)

    # Update the progress bar
    progress_bar.update(1)
    # Add a small delay to see the progress
    time.sleep(0.1)

# Close the progress bar
progress_bar.close()

# Write block lists to output files if they contain data
if len(block_list) > 0:
    pd.DataFrame(block_list).to_csv('/home/$USER/block_list.txt', header=False, index=False)
if len(company_list) > 0:
    pd.DataFrame(company_list).to_csv('/home/$USER/company_list.txt', header=False, index=False)
