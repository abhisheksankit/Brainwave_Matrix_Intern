import re
import requests
from urllib.parse import urlparse

def is_suspicious_url(url):
    suspicious_keywords = ['login', 'verify', 'update', 'secure', 'banking', 'account', 'free', 'offer', 'password']
    domain = urlparse(url).netloc.lower()

    for keyword in suspicious_keywords:
        if keyword in url.lower():
            return True

    if '-' in domain or domain.count('.') > 2:
        return True

    return False

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[+] {url} is reachable.")
        else:
            print(f"[-] {url} is unreachable or returned status {response.status_code}")
    except Exception as e:
        print(f"[!] Error: {e}")

    if is_suspicious_url(url):
        print(f"[!] {url} might be a phishing link!")
    else:
        print(f"[+] {url} seems safe.")

if __name__ == "__main__":
    user_url = input("Enter the URL to scan: ")
    if not user_url.startswith("http"):
        user_url = "http://" + user_url
    check_url(user_url)
