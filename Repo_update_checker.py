import requests
import os
import time
import urllib3

# Suppress the specific SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# URL of the file to monitor
url = "https://raw.githubusercontent.com/MehPandaHu/testing/main/test"
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

def show_added_lines(old_content, new_content):
    old_lines = set(old_content.splitlines())
    new_lines = set(new_content.splitlines())
    added_lines = new_lines - old_lines
    return '\n'.join(added_lines)

def check_for_updates():
    latest_content = get_latest_content()
    if latest_content is None:
        return

    last_content = read_last_content()

    if last_content is None:
        write_last_content(latest_content)
        print("Initial content fetched and stored.")
    elif latest_content != last_content:
        print("Update detected!")
        added_lines = show_added_lines(last_content, latest_content)
        write_last_content(latest_content)
        print(f"Added lines:\n{added_lines}")
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
