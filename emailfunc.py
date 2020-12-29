# this file defines functions that allow the main program to send emails
# to do: template out the content of the email

import smtplib, ssl

def sendemail(server, sender, password, receiver, msg, port=465):
	context = ssl.create_default_context()
	
	try:	
		with smtplib.SMTP_SSL(server, port, context) as serv:
			serv.login(sender, password)
			serv.sendmail(sender, receiver, msg.as_string())
			return "Email sent successfully"
	except smtplib.SMTPAuthenticationError:
		return "Error: Incorrect Credentials (SMTP Authentication Error)"
	except smtplib.SMTPException:
		return "Error: Could not send email. (SMTP Exception)"
	except (ssl.SSLError, smtplib.SMTPServerDisconnected):
		return "Error: SSL or SMTP Connection Error"
	#except:
	#	return "Unexpected Error :( "