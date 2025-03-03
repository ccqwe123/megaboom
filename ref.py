import requests
import secrets
import string
import time
import concurrent.futures

def generate_solana_address():
    """Generate a random Solana address."""
    characters = string.ascii_uppercase + string.digits
    address = ''.join(secrets.choice(characters) for _ in range(44))
    # Ensure the address starts with a valid character (only uppercase letters and numbers)
    while address[0] not in string.ascii_uppercase + '23456789':
        address = ''.join(secrets.choice(characters) for _ in range(44))
    return address

def send_request(ref_code):
    """Send a GET request to the Meganet API."""
    base_url = "https://api.meganet.app/wallets"
    solana_address = generate_solana_address()
    params = {
        "address": solana_address,
        "refcode": ref_code
    }
    headers = {
        "sec-ch-ua-platform": "Windows",
        "sec-ch-ua": 'Not A;Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        "sec-ch-ua-mobile": "0",
        "Origin": "Meganet",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "Meganet",
        "Accept-Language": "en-US,en;q=0.9"
    }
    try:
        response = requests.get(base_url, params=params, headers=headers)
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def get_number_of_workers():
    while True:
        try:
            num_workers = int(input("Enter the number of workers: "))
            if num_workers <= 0:
                print("Please enter a positive integer.")
            else:
                return num_workers
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    ref_code = input("Enter your ref code: ")
    num_workers = get_number_of_workers()
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        while True:
            futures = [executor.submit(send_request, ref_code) for _ in range(num_workers)]
            for future in concurrent.futures.as_completed(futures):
                future.result()
            time.sleep(1)  # wait 1 second before sending the next batch of requests

if __name__ == "__main__":
    main()