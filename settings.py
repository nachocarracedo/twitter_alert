# twitter keys and tokens API
APP_KEY = ""
APP_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

# email info
EMAIL_USERNAME = ""
EMAIL_PASSWORD = ""
EMAIL_TO = "" #recipient
SMTP_SERVER = ""

# accounts and keywords(case insensitive)
TWITTER_AC_MONITOR = []
KEYWORDS = [] 

try:
	from private import *
except Exception:
	pass