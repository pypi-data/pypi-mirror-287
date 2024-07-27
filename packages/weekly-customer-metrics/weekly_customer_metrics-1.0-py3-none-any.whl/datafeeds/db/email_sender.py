import smtplib
import ssl
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

class EmailSender:
    def __init__(self, sender_email, password, smtp_server="us-smtp-outbound-1.mimecast.com", port=587):
        self.sender_email = sender_email
        self.password = password
        self.smtp_server = smtp_server
        self.port = port

    def send_email(self, receiver_email, message):
        try:
            logging.info("Connecting to the server...")
            with smtplib.SMTP(self.smtp_server, self.port, timeout=200) as server:
                logging.info("Connected to the server.")
                
                server.ehlo()
                logging.info("EHLO done.")
                
                server.starttls(context=ssl.create_default_context())
                logging.info("STARTTLS done.")
                
                server.ehlo()
                logging.info("EHLO done again.")
                
                logging.info("Logging in...")
                server.login(self.sender_email, self.password)
                logging.info("Logged in successfully.")
                
                # Create the email message
                msg = MIMEMultipart()
                msg['From'] = self.sender_email
                msg['To'] = ", ".join(receiver_email)
                msg['Subject'] = " Weekly Customer Metrics "
                
                # Attach the message body
                msg.attach(MIMEText(message, 'html'))

                logging.info("Sending email...")
                server.sendmail(self.sender_email, receiver_email, msg.as_string())
                logging.info("Email sent successfully.")
                print("Email sent successfully.")
        except smtplib.SMTPException as e:
            logging.error(f"SMTP error occurred: {e}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")







