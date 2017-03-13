class Twitter_log_csv:
			
	def save_csv(self, last_tweets_df,tweet_hits_df):
		# save last tweet				
		last_tweets_df.to_csv("./csv/last_tweet.csv", index=False, encoding='utf-8')
		# save alerts sent
		tweet_hits_df.to_csv("./csv/tweet_hits.csv", index=False)