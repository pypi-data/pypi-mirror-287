import pandas as pd
import smtplib
import ssl
import redshift_connector
import os

import logging 


redshift_password = os.environ.get('REDSHIFT_PASSWORD_NEW')
redshift_username = os.environ.get('USERNAME')


prod_conn = redshift_connector.connect(

    host="le-us-e1-prod-edw-redshift-endpoint-jd64e5glhvekqswwxmyh.ct0yyph18ii7.us-east-1.redshift.amazonaws.com",

    database="nzpvw001",

    cluster_identifier="le-us-e1-prod-edw-redshift",

    client_id="8e04d88e-fd39-4cd3-8fc5-5cd2d7db6248",

    port=5439,

    ssl=True,

    iam=True,

    db_user="",

    idp_tenant="682a61d2-c906-4fa3-a505-4c7cd3da5572",

    credentials_provider="BrowserAzureCredentialsProvider",

    region="us-east-1",

    sslmode="verify-full",

    user=redshift_username, 

    password=redshift_password 
)
    
def auto_rollback(cursor, func):

    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except Exception as e:
            cursor._execute("ROLLBACK;")
            raise e

    return wrapper


prod_cursor = prod_conn.cursor()
prod_cursor._execute = prod_cursor.execute
prod_cursor.execute = auto_rollback(prod_cursor, prod_cursor.execute)



### Function to Send Emails 

def send_email(SENDER_EMAIL, RECEIVER_EMAIL,PASSWORD, message,SMTP_SERVER="us-smtp-outbound-1.mimecast.com",PORT=587):
    try:
        logging.info("Connecting to the server...")
        with smtplib.SMTP(SMTP_SERVER, PORT, timeout=200) as server:
            logging.info("Connected to the server.")
            
            server.ehlo()
            logging.info("EHLO done.")
            
            server.starttls(context=ssl.create_default_context())
            logging.info("STARTTLS done.")
            
            server.ehlo()
            logging.info("EHLO done again.")
            
            logging.info("Logging in...")
            server.login(SENDER_EMAIL, PASSWORD)
            logging.info("Logged in successfully.")
            
            logging.info("Sending email...")
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
            print("Email sent successfully.")
    except smtplib.SMTPException as e:
        logging.error(f"SMTP error occurred: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")