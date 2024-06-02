import requests
import os
import time
import urllib3
import yaml

# Suppress the specific SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URL of the raw YAML file to monitor
url = "https://raw.githubusercontent.com/SigmaHQ/sigma/master/rules/windows/network_connection/net_connection_win_domain_crypto_mining_pools.yml"
# File to store the last content
last_content_file = "last_content.txt"

def get_latest_content():
    try:
        response = requests.get(url, verify=False)  # Disable SSL verification
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        print(f"Error fetching the latest content: {e}")
        return None

def read_last_content():
    if os.path.exists(last_content_file):
        with open(last_content_file, "r") as file:
            return file.read().strip()
    return None

def write_last_content(content):
    with open(last_content_file, "w") as file:
        file.write(content)

def parse_destination_hostnames(yaml_content):
    parsed_yaml = yaml.safe_load(yaml_content)
    return set(parsed_yaml['detection']['selection']['DestinationHostname'])

def check_for_updates():
    latest_content = get_latest_content()
    if latest_content is None:
        return

    last_content = read_last_content()

    latest_hostnames = parse_destination_hostnames(latest_content) if latest_content else set()
    last_hostnames = set(last_content.splitlines()) if last_content else set()

    if not last_hostnames:
        write_last_content('\n'.join(latest_hostnames))
        print("Initial content fetched and stored.")
    elif latest_hostnames != last_hostnames:
        added_lines = latest_hostnames - last_hostnames
        if added_lines:
            print("Update detected!")
            added_lines_str = '\n'.join(added_lines)
            print(f"Added lines:\n{added_lines_str}")
        write_last_content('\n'.join(latest_hostnames))
    else:
        print("No updates detected.")

if __name__ == "__main__":
    print("###############################################")
    print("#                                             #")
    print("#             Created by MehPandaHu           #")
    print("#                                             #")
    print("###############################################")
    while True:
        check_for_updates()
        # Check for updates every 2 minutes
        time.sleep(120)
