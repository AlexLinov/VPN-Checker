# IP Analysis Script

This script analyzes a list of IP addresses and generates block lists and company lists based on the analysis. It checks if each IP address is a VPN, proxy, Tor node, or relay, and adds them to the respective block lists. Additionally, it creates a company list of the organizations associated with the IP addresses, excluding certain companies.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed:

- Python 3
- openpyxl library
- requests library
- pandas library
- tqdm library

You can install the necessary libraries using pip:

```shell
pip install -r requirements.txt

Usage
1. Clone the repository or download the script file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script with the following command:

python script.py <input_file_location>
