import requests
import time

# Set the base URL
BASE_URL = "https://api.meganet.app/wallets/task/"

# Define headers
HEADERS = {
    "Host": "api.meganet.app",
    "Connection": "keep-alive",
    "sec-ch-ua-platform": '"Windows"',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "Origin": "https://meganet.app",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://meganet.app/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,fil;q=0.8"
}

def fetch_wallet_task(wallet_id):
    url = f"{BASE_URL}{wallet_id}/oneHundredNode"
    try:
        response = requests.patch(url, headers=HEADERS)
        if response.status_code == 200:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Success! Check your EXP!")
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Failed - Status Code:", response.status_code)
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error:", e)

def main():
    wallet_id = input("Enter Wallet ID: ").strip()

    print(f"Starting task fetch for wallet: {wallet_id}")
    
    try:
        while True:
            fetch_wallet_task(wallet_id)
            time.sleep(5)  # 5 seconds interval
    except KeyboardInterrupt:
        print("\nBot stopped by user.")

if __name__ == "__main__":
    main()
