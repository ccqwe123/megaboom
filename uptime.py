import requests
import time

# Set the base URL
BASE_URL = "https://api.meganet.app/wallets/uptime/"
POINTS = "https://api.meganet.app/points/point-today/67c1bbab81277b8b78cceab7"
AUTH_URL = "https://meganet.app/api/auth/session"
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

AUTH_HEADER = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Cookie": "__Host-next-auth.csrf-token=de0023814effe3c1925dbf143bf38bb6fad64af14a64e12e357e3f12b60ffa67%7C3cd80666be878c1791fc19567c646c18015637b03a78f76b66b7f40e530934c6; __Secure-next-auth.callback-url=https%3A%2F%2Fmeganet.app; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..PtKPSfpu07L7GKXa.bery-gjIpw59Oifd9LXZx60wtklvhyM4qaulg0dsxVRmIIp0T9J2SEvYX7Yu7ZswzkcE3xNmLbTn5_ZlvfFwLp5A45Yg6rnoUpwIvBrfYqkTBpAEbMAnqjoUfqax23sUYfdclcdBVekA9nXAlv4nCVhE2PwaYnisfpJ-Uzjp68bdpxl9vCeX9JSyWBXB-lG3VKfSCEjiS3eeysJTo_NaBQ25W6n_SDIGv9ucGK4duSxyurOWylXCEQMwn3fxfXd2J8Q18ux_xG3cbjEiLGhk4TvdFX0SbH-j59d_PE_ryCPQjYo8gbUZX4jxmf_c9oJxtcKMWTzr5v1vsKE0I52h6Bmd0PpPhRUEa19EZveLVcy3H-qtrEsigAiYhI8xTdQGC0i9hFknESbi_EwdyLdqEF3DCHpheCvo4gBUg_Y-0gtL2dw_JCcddTnOpByJVYHPWKOR82MokIm4GsIM_mr6TlmrPaPr2SsZ7cRCvY0UKaxOp7GlHrEzhVlZswOJE_OlO_adyE-_xQ.hKL0HXbbXzJobXaFlQtNLA",
    "Host": "meganet.app",
    "Referer": "https://meganet.app/node-management",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Brave";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}
def fetch_wallet_task(wallet_id):
    url = f"{BASE_URL}{wallet_id}"
    try:
        response = requests.options(url, headers=HEADERS)
        if response.status_code == 200:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Uptime Updated!")
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Success - Status Code:", response.status_code)
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error:", e)

def fetch_uptime_task(wallet_id):
    authUser()
    url = f"{BASE_URL}{wallet_id}"
    try:
        response = requests.patch(url, headers=HEADERS)
        if response.status_code == 200:
            fetch_wallet_task(wallet_id)
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Uptime Updated!")
            getpoints()
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Failed - Status Code:", response.status_code)
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error:", e)

def getpoints():
    url = f"{POINTS}"
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] current Points: {response.json()['pointsFarmToday']}")
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Failed - Status Code:", response.status_code)
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error:", e)

def authUser():
    url = f"{AUTH_URL}"
    try:
        response = requests.get(url, headers=AUTH_HEADER)
        if response.status_code == 200:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] User Authenticated: {response.json()['username']}")
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Failed - Status Code:", response.status_code)
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error:", e)

def main():
    wallet_id = input("Enter Wallet ID: ").strip()

    print(f"Starting task fetch for wallet: {wallet_id}")
    
    try:
        while True:
            fetch_uptime_task(wallet_id)
            time.sleep(5)  # 5 seconds interval
    except KeyboardInterrupt:
        print("\nBot stopped by user.")

if __name__ == "__main__":
    main()
