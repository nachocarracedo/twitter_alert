import settings
import sys
import os.path
import pandas as pd

from classes.twitter_scan import Twitter_scan
from classes.twitter_log import Twitter_log_csv
from classes.twitter_email import Twitter_email

if __name__ == "__main__":
	
	#### scan
	print("Scanning ...")
	ts = Twitter_scan(settings.APP_KEY,
			settings.APP_SECRET,
			settings.OAUTH_TOKEN,
			settings.OAUTH_TOKEN_SECRET)
			
	# is incremental search? 
	incremental = False
	if os.path.isfile("./csv/last_tweet.csv"):
		last_tweet = pd.read_csv("./csv/last_tweet.csv", encoding='utf-8')
		incremental = True		
	
	# scan tweets	
	try:				
		logs = ts.twitter_hits(settings.TWITTER_AC_MONITOR,
						settings.KEYWORDS,
						incremental,
						last_tweet)
	except Exception as e:
		print("***** Error retrieving the tweets ****")
		print(e)
		sys.exit(1)
		
	last_tweets_df = logs[0]
	tweet_hits_df = logs[1]
		
		
	#### send notifications
	tweets_to_send_df = tweet_hits_df[tweet_hits_df.sent == 0]
	
	if tweets_to_send_df.shape[0] > 0:
		# generate email body
		msg = "Scan found matches!! :\n\n"
		for t in range(tweets_to_send_df.shape[0]):
			msg = msg + tweets_to_send_df.festival_id.iloc[t] + " --- " + tweets_to_send_df.date.iloc[t] + "\n"
			msg = msg + tweets_to_send_df.tweet_text_hit.iloc[t] + "\n\n"
		
		# send mail	
		tmail = Twitter_email(settings.EMAIL_USERNAME,
						settings.EMAIL_PASSWORD,
						settings.SMTP_SERVER,
						settings.EMAIL_TO,
						tweets_to_send_df)
						
		print("Sending email with hits ...")
		try:
			tmail.send_email(msg)
		except Exception as e:
			print ('Something went wrong sending the email:')
			print (e)
		else: 
			tweet_hits_df["sent"] = tweet_hits_df["sent"].map(lambda x: 1 if x==0 else x)
			
	else:
		print("Matches NOT found ... ")
	
	
	#### save logs
	print("Saving logs ... ")	
	Twitter_log_csv().save_csv([last_tweets_df,tweet_hits_df],['last_tweet.csv','tweet_hits.csv'])
	print("Done!")
	