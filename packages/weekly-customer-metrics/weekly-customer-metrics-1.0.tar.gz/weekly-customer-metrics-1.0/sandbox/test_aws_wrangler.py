import boto3
import awswrangler as wr

class RedshiftConnector:
    def __init__(self, profile_name, glue_connection, region_name='us-east-1'):
        """
        Initialize the RedshiftConnector with the specified AWS profile, region, and Glue connection name.
        
        :param profile_name: The AWS profile name to use for the session.
        :param glue_connection: The Glue connection name for Redshift.
        :param region_name: The AWS region name.
        """
        self.boto3_session = boto3.Session(profile_name=profile_name, region_name=region_name)
        self.glue_connection = glue_connection
        
        glue_client = self.boto3_session.client('glue')
        connection_details = glue_client.get_connection(Name=glue_connection)['Connection']['ConnectionProperties']
        
        if 'JDBC_CONNECTION_URL' not in connection_details:
            raise KeyError("JDBC_CONNECTION_URL not found in Glue connection properties.")
        
        self.redshift_connection = wr.redshift.connect(connection=glue_connection, boto3_session=self.boto3_session)

    def read_sql_query(self, query):
        """
        Execute a SQL query on the Redshift cluster and return the result as a DataFrame.
        
        :param sql_query: The SQL query to execute.
        :return: A pandas DataFrame containing the query results.
        """
        df = wr.redshift.read_sql_query(sql=query, con=self.redshift_connection)
        return df


redshift_connector = RedshiftConnector(profile_name='dataadmin', glue_connection='nmdeshi_nzpvw001')


query = """
select  *
from lehub.fct_dmd_item fdi
Limit 5
"""

df= redshift_connector.read_sql_query(query)
print(df) 









