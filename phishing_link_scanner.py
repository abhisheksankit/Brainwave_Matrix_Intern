import requests
from urllib.parse import urlparse
import whois

def check_url(url):
    try:
        print(f"\nScanning: {url}")
        response = requests.get(url, timeout=5)
        domain = urlparse(url).netloc
        domain_info = whois.whois(domain)

        if domain_info.creation_date:
            print(f"[+] Domain Age: {domain_info.creation_date}")
        else:
            print("[-] Domain age could not be found.")

        if "login" in url or "verify" in url or "update" in url:
            print("[!] Suspicious keywords found in URL.")
        else:
            print("[+] No suspicious keywords found.")

    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    user_url = input("Enter the URL to scan: ")
    check_url(user_url)
