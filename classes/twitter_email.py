import smtplib

class Twitter_email:

	def __init__(self, username, password, smtp_server, email_to, twitter_hits):
		self.server = smtplib.SMTP(smtp_server)
		self.username = username
		self.password = password
		self.email_to = email_to
		self.twitter_hits = twitter_hits
							
	def send_email(self):
	
		msg = "Twitter scan found matches!! :\n\n"
		
		# create email body text
		for t in range(self.twitter_hits.shape[0]):
			msg = msg + self.twitter_hits.festival_id.iloc[t] + " --- " + self.twitter_hits.date.iloc[t] + "\n"
			msg = msg + self.twitter_hits.tweet_text_hit.iloc[t] + "\n\n"
			From = self.username 
			to = self.email_to 
			subject = 'Twitter hit alert'  
			body = msg
			email_text = """  
			From: %s  
			To: %s  
			Subject: %s

			%s
			""" % (From, to, subject, body)

		# mail send
		self.server.ehlo()
		self.server.starttls()
		self.server.login(self.username,self.password)
		self.server.sendmail(self.username, self.email_to, email_text)
		self.server.quit()
		print("Email sent successfully")
        
		