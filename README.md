# bakabt_auto-login_prune-prevention.py (THIS HAS BEEN PATCHED - NOT RELEASING MY PERSONAL FIX TO AVOID THAT GETTING PATCHED...) NOTE: THIS SCRIPT WAS NEVER FOR ANY ILL PURPOSES AND HAD NO MALICIOUS INTENT; IT ONLY EXISTED IN ORDER FOR THOSE PEOPLE, PEOPLE THAT CARE ABOUT THEIR ACCOUNT, TO HELP MAKE SURE THAT THEY KEEP IT, IF THEY WERE TOO BUSY WITH LIFE TO LOG IN OFTEN ENOUGH TO PREVENT ITS PRUNING - THAT IS ALL...  CHEERS.
bakabt_auto-login_prune-prevention.py is a cli way to log in to your BakaBT account to prevent pruning; you can set up a crontab entry and have it run once a day to log you in automatically.  This is a: Python script.

#

This code is using the requests library to send an HTTP request to the Bakabt website. The if statement at the beginning determines whether the code should log the user out or log the user in.

If scenario is 1, the code sends a GET request to the /logout.php URL to log the user out. It then sends a GET request to the login page URL and parses the HTML response using the BeautifulSoup library. It then searches the parsed HTML for an element with the tag a and the attribute href="/recover.php", and if it finds this element, it prints "Logged out successfully". If it doesn't find this element, it prints "Logout failed".

If scenario is not 1, the code sets up an HTTP header with a Cookie field and a User-Agent field, and a payload with the login credentials. It then sends a POST request to the login page URL with these headers and payload, and prints the HTTP status code of the response. It also parses the HTML of the response and searches for an element with the tag li and the class welcomeback. If it finds this element, it prints "Logged in successfully". If it doesn't find this element, it prints "Login failed".

#

To check your system logs for the cron process to see if the script has been been running successfully, at the console type this: grep bakabt_auto-login_prune-prevention.py /var/log/syslog

Example log output: \
Dec 26 00:00:02 Your_System CRON[15098]: (YOU) CMD (python3 /home/YOU/bakabt_auto-login_prune-prevention.py) \
Dec 27 00:00:02 Your_System CRON[17505]: (YOU) CMD (python3 /home/YOU/bakabt_auto-login_prune-prevention.py) \
Dec 28 00:00:02 Your_System CRON[19902]: (YOU) CMD (python3 /home/YOU/bakabt_auto-login_prune-prevention.py) \
Dec 29 00:00:02 Your_System CRON[22302]: (YOU) CMD (python3 /home/YOU/bakabt_auto-login_prune-prevention.py) \
Dec 30 00:00:02 Your_System CRON[24662]: (YOU) CMD (python3 /home/YOU/bakabt_auto-login_prune-prevention.py) \
Dec 31 00:00:01 Your_System CRON[28674]: (YOU) CMD (python3 /home/YOU/bakabt_auto-login_prune-prevention.py)

As you can see, it runs once a day.

#

pip install -r requirements.txt
