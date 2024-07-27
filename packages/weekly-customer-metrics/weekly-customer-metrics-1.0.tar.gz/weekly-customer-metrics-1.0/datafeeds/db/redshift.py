import pandas as pd
import smtplib
import ssl
import redshift_connector
import os
from spark_lib.config.redshift_config import RedshiftConfig
import logging 

redshift_config = RedshiftConfig(url="le-us-e1-prod-edw-redshift-endpoint-jd64e5glhvekqswwxmyh.ct0yyph18ii7.us-east-1.redshift.amazonaws.com", secret_name="development/integration_tests/redshift_test")


redshift_password = redshift_config.get_secret_data.get("password")
redshift_username = redshift_config.get_secret_data.get("user")

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



