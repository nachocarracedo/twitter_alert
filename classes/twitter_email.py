import smtplib

class Twitter_email:

	def __init__(self, username, password, smtp_server, email_to, twitter_hits):
		""" Init connection with email server"""
		self.server = smtplib.SMTP(smtp_server)
		self.username = username
		self.password = password
		self.email_to = email_to
		self.twitter_hits = twitter_hits
							
	def send_email(self, text):
		""" sends email with text as body """
		subject = "Twitter ALERT"
		self.server.ehlo()
		self.server.starttls()
		self.server.login(self.username,self.password)
		message = 'Subject: {}\n\n{}'.format(subject, text)
		self.server.sendmail(self.username, self.email_to, message)
		self.server.quit()
		print("Email sent successfully")
        
		