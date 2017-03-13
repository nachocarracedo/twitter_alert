from twython import Twython
import pandas as pd
import string
import os.path

class Twitter_scan:

	def __init__(self, APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET):
		""" init twitter API connection"""	
		self.twitter = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
		self.tweet_text_hit= []
		self.tweet_date_hit= []
		self.tweet_id_hit = []
		self.tweet_account_hit = []
		self.last_tweet_id = []
							
	def twitter_hits(self, accounts, keywords, incremental, last_t_df=pd.DataFrame()):
		""" Scans accounts for keywords. If incremental == False
		it will scan last 2 tweets. Otherwise it will scan only new tweets.
		Returns 2 dataframes: last_tweet_df: id of last tweet scanned,
		th2_df: info of tweets with keyworks (text, creation)"""		
			
		# Get and scan tweets 
		for festival_id in accounts:
			if incremental: 
				lt = int(last_t_df[last_t_df["festival"]==festival_id]["last_tweet_id"].iloc[0])
				tweets = self.twitter.get_user_timeline(screen_name=festival_id,
											since_id=lt,
											exclude_replies=True)				
			else:
				tweets = self.twitter.get_user_timeline(screen_name=festival_id,
											count=2,
											exclude_replies=True)
										
			# get last tweet id 
			if len(tweets) > 0:
				self.last_tweet_id.append(tweets[0]["id"])
			else:
				self.last_tweet_id.append(lt)
			   
			# get hits
			for t in tweets:
				text = t["text"].lower()
				if any(kb in text for kb in keywords):
					self.tweet_account_hit.append(festival_id)
					printable = set(string.printable)
					self.tweet_text_hit.append("".join(list(filter(lambda x: x in printable, t["text"]))))		
					self.tweet_date_hit.append(t["created_at"])
					self.tweet_id_hit.append(t["id"])
					
		# last tweet id to dataframe
		last_t_df = pd.DataFrame({'festival':accounts, 'last_tweet_id':self.last_tweet_id})
		
		# hits to dataframe
		th2_df = pd.DataFrame({'festival_id':self.tweet_account_hit,
					'tweet_text_hit':self.tweet_text_hit,
					'date':self.tweet_date_hit,
					'tweet_id':self.tweet_id_hit})
		th2_df["sent"] = 0			
		
			
		#return dataframes
		return (last_t_df,th2_df)