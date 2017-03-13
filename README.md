## GIGTAT twitter alerts

This script will check twitter accounts and will scan tweets looking for keywords. If keywords are found an email is sent with the twitter account, time of posting, and tweet text.

First time the script is run, if `./csv/last_tweet.csv` doesn't exist, the script will check the last 2 tweets for each account. Following executions of the script will check only new tweets.

A log of all tweets that have keywords in it will be saved in `./csv/tweet_hits.csv`.


### USE 

1) Copy all files and folders of this repository into a folder.

2) Create a Twitter user account if you don't have one already.
Go to *https://apps.twitter.com/* and log in with your Twitter user account. 

3) Get dev account under same name and get your twitter keys:

* Click “Create New App”
* Fill out the form, agree to the terms, and click “Create your Twitter application”
* In the next page, click on “Keys and Access Tokens” tab, and copy your “API key” and “API secret”. Scroll down and click “Create my access token”, and copy your “Access token” and “Access token secret”. 


4) Open settings.py and:

* Add your twitter keys and access tokens from *https://apps.twitter.com/*.
* Add email credentials and recipient to settings.py (you may need to enable access for less secure apps with your email provider [E.g. gmail: *https://www.google.com/settings/security/lesssecureapps*])
* Add SMTP server used to send email [E.g. gmail: *smtp.gmail.com:587*]
* Add twitter accounts to be scanned and keywords to look for(case insensitive).

5) Make sure you are running Python 3.X and install libraries in requirements.txt (`pip install -r /path/to/requirements.txt`). Use `pip install libraryname` to install any other library.

6) Run script manually (`python twitter_alert_main.py`) or add it to cron to run every X min [Every 15 min: `*/15 * * * * /path/to/twitter_alert_main.py`]