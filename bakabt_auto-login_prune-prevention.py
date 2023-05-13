# To RUN: at console, type: python3 bakabt_auto-login_prune-prevention.py
# Set up an @daily crontab entry for it; to log in once a day
# e.g. @daily python3 /home/YourUser/bakabt_auto-login_prune-prevention.py
# crontab -l, crontab -e & edit+save, crontab -l
# pip install requests
# pip install beautifulsoup4
# precaution:
# pip3 install requests
# pip3 install beautifulsoup4

import requests
from bs4 import BeautifulSoup

URL = "https://bakabt.me/"
USERNAME = "YOUR_USERNAME"
PASSWORD = "YOUR_PASSWORD"
scenario = 0

if scenario == 1:
    logout_response = requests.get("https://bakabt.me/logout.php")
    print(logout_response.text)
    login_page_response = requests.get(URL)
    print(login_page_response.text)
    soup = BeautifulSoup(login_page_response.text, "html.parser")
    recover_element = soup.find("a", href="/recover.php")
    if recover_element is not None:
        print("Logged out successfully")
    else:
        print("Logout failed")
else:
    headers = {
        "Cookie": "name=value",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    }
    payload = {
        "username": USERNAME,
        "password": PASSWORD,
        "loginKey": ""
    }
    response = requests.post(URL, headers=headers, data=payload)
    print(response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")
    print(response.text)
    print(soup.prettify())

    welcomeback_element = soup.find("li", class_="welcomeback")
    if welcomeback_element is not None:
        print("Logged in successfully")
    else:
        print("Login failed")

#input("Press Enter to continue...")
