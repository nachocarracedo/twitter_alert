import pandas as pd
import os.path

class Twitter_log_csv:
	def __init__(self, folder):
		""" init dataframes for logs"""	
		self.folder = "./" + folder + "/"
		
		if os.path.isfile("./csv/last_tweet.csv"):
			self.last_tweets_df = pd.read_csv(self.folder + "last_tweet.csv",
										encoding='utf-8')
		else:
			self.last_tweets_df = pd.DataFrame()			
			
		if os.path.isfile("./csv/tweet_hits.csv"):
			self.tweet_hits_df =  pd.read_csv(self.folder + "tweet_hits.csv",
										encoding='utf-8')
		else:
			self.tweet_hits_df = pd.DataFrame()
		
				
	def save_csv(self):
		""" save dataframes as csv files"""	
		self.last_tweets_df.to_csv(self.folder + "last_tweet.csv", index=False, encoding='utf-8')
		self.tweet_hits_df.to_csv(self.folder + "tweet_hits.csv", index=False, encoding='utf-8')
			
	def incremental_log(self):
		""" check if incremental log exists"""
		if os.path.isfile(self.folder + "last_tweet.csv"):
			return True
		else:
			return False
			
	def hit_log(self):
		""" check if incremental log exists"""
		if os.path.isfile(self.folder + "tweet_hits.csv"):
			return True
		else:
			return False	
			
	def update_hit_log(self, hits_df):
		""" update hit log"""
		if self.hit_log():
			self.tweet_hits_df = pd.concat([self.tweet_hits_df, hits_df])
		else:
			self.tweet_hits_df = hits_df
		