import settings
import sys

from classes.twitter_scan import Twitter_scan
from classes.twitter_log import Twitter_log_csv
from classes.twitter_email import Twitter_email

if __name__ == "__main__":
	
	# scan
	print("Scanning ...")
	ts = Twitter_scan(settings.APP_KEY,
			settings.APP_SECRET,
			settings.OAUTH_TOKEN,
			settings.OAUTH_TOKEN_SECRET)
	try:				
		logs = ts.twitter_hits(settings.TWITTER_AC_MONITOR,
					settings.KEYWORDS)
	except Exception as e:
		print("***** Error retrieving the tweets ****")
		print(e)
		sys.exit(1)
					
	last_tweets_df = logs[0]
	tweet_hits_df = logs[1]
		
	# send notifications
	tweets_to_send_df = tweet_hits_df[tweet_hits_df.sent == 0]
	
	if tweets_to_send_df.shape[0] > 0:
		tmail = Twitter_email(settings.EMAIL_USERNAME,
						settings.EMAIL_PASSWORD,
						settings.SMTP_SERVER,
						settings.EMAIL_TO,
						tweets_to_send_df)
		print("Sending email with hits ...")
		
		try:
			tmail.send_email()
		except Exception as e:
			print ('Something went wrong sending the email:')
			print (e)
		else:
			tweet_hits_df["sent"] = tweet_hits_df["sent"].map(lambda x: 1 if x==0 else x)
						
	else:
		print("Matches NOT found ... ")
	
	# save logs
	print("Saving logs ... ")	
	save_log = Twitter_log_csv()
	save_log.save_csv(last_tweets_df,tweet_hits_df)
	print("Done!")
	