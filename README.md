# bakabt_auto-login_prune-prevention.py
bakabt_auto-login_prune-prevention.py is a cli way to log in to your BakaBT account to prevent pruning; you can set up a crontab entry and have it run once a day to log you in.  This is a Python script.

#

This code is using the requests library to send an HTTP request to the Bakabt website. The if statement at the beginning determines whether the code should log the user out or log the user in.

If scenario is 1, the code sends a GET request to the /logout.php URL to log the user out. It then sends a GET request to the login page URL and parses the HTML response using the BeautifulSoup library. It then searches the parsed HTML for an element with the tag a and the attribute href="/recover.php", and if it finds this element, it prints "Logged out successfully". If it doesn't find this element, it prints "Logout failed".

If scenario is not 1, the code sets up an HTTP header with a Cookie field and a User-Agent field, and a payload with the login credentials. It then sends a POST request to the login page URL with these headers and payload, and prints the HTTP status code of the response. It also parses the HTML of the response and searches for an element with the tag li and the class welcomeback. If it finds this element, it prints "Logged in successfully". If it doesn't find this element, it prints "Login failed".

#

pip install -r requirements.txt
