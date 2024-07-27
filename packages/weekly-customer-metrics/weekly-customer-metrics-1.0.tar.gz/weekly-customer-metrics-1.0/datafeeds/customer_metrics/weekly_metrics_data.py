import pandas as pd
import datetime
import warnings
import os
import smtplib
import ssl
import logging
warnings.filterwarnings("ignore")

import sys
sys.path.insert(0, r'C:\Users\nmdeshi\weekly_customer_metrics\datafeeds\db')
from redshift import *
from email_sender import EmailSender
from sql_queries import *

class WeeklyMetrics:
    def __init__(self):
        self.current_date = datetime.date.today().strftime('%Y-%m-%d')
        self.sender_email = "customer_analytics@landsend.com"
        self.receiver_email = ["neeraj.deshingkar@landsend.com" , "meredith.ginther@landsend.com" , "christoph.seifert@landsend.com"]
        self.password = os.environ.get('email_password')

    def connect_to_redshift(self):
        pass

    def run_queries(self):
        print("Running queries to get weekly metrics data")
        self.prod_df = pd.read_sql_query(UAT_QUERY_3, prod_conn)
        self.prod_df_23 = pd.read_sql_query(UAT_QUERY_4, prod_conn)
        self.margin_df_24 = pd.read_sql_query(UAT_QUERY_5, prod_conn)
        self.margin_df_24_ = pd.read_sql_query(UAT_QUERY_6, prod_conn)
        self.margin_df_23 = pd.read_sql_query(UAT_QUERY_7, prod_conn)
        self.margin_df_23_ = pd.read_sql_query(UAT_QUERY_8, prod_conn)
        self.ntb_this_week = pd.read_sql_query(UAT_QUERY_9, prod_conn)
        self.ntb_this_week_ = pd.read_sql_query(UAT_QUERY_10, prod_conn)
        self.ntb_this_week_ly = pd.read_sql_query(UAT_QUERY_11, prod_conn)
        self.ntb_this_week_ly_ = pd.read_sql_query(UAT_QUERY_12,prod_conn)
        
        self.ntb_acquisition_this_week = pd.read_sql_query(UAT_QUERY_13,prod_conn)
        self.ntb_acquisition_this_week_ly = pd.read_sql_query(UAT_QUERY_14,prod_conn)
        self.ntb_acquisition_shifted_week = pd.read_sql_query(UAT_QUERY_15,prod_conn)
        self.ntb_acquisition_shifted_week_ly = pd.read_sql_query(UAT_QUERY_16,prod_conn)
        self.reactivated_acquisition_this_week = pd.read_sql_query(UAT_QUERY_17,prod_conn)
        self.reactivated_acquisition_this_week_ly = pd.read_sql_query(UAT_QUERY_18,prod_conn)
        self.reactivated_acquisition_shifted_week = pd.read_sql_query(UAT_QUERY_19,prod_conn)
        self.reactivated_acquisition_shifted_week_ly = pd.read_sql_query(UAT_QUERY_20,prod_conn)

    def calculate_metrics(self):
        self.prod_df_23['first_dt_ytd'] = pd.to_datetime(self.prod_df_23['first_dt_ytd'])
        self.prod_df_23_16 = self.prod_df_23[self.prod_df_23['first_dt_ytd'].isin(week_dates_23)]
        matrix_table_23 = self.prod_df_23_16.groupby(['recency','frequency'])['hshld'].nunique().unstack().sort_values(by='recency',   ascending=True).reset_index()
        new_order = [0, 4, 1, 2, 3]
        matrix_table_23 = matrix_table_23.reindex(new_order)
        matrix_table_23.set_index('recency', inplace=True)
        self.weekly_metric_2023 = matrix_table_23['1x'].sum()
        self.weekly_metric_2023_5x = matrix_table_23['5x+'].sum()

        self.prod_df_23_17 = self.prod_df_23[self.prod_df_23['first_dt_ytd'].isin(week_dates_23_mod)]
        matrix_table_23_ = self.prod_df_23_17.groupby(['recency','frequency'])['hshld'].nunique().unstack().sort_values(by='recency', ascending=True).reset_index()
        matrix_table_23_ = matrix_table_23_.reindex(new_order)
        matrix_table_23_.set_index('recency', inplace=True)
        self.shifted_weekly_metric_2023 = matrix_table_23_['1x'].sum()
        self.shifted_weekly_metric_2023_5x = matrix_table_23_['5x+'].sum()

        self.prod_df['first_dt_ytd'] = pd.to_datetime(self.prod_df['first_dt_ytd'])
        self.prod_df_24_17 = self.prod_df[self.prod_df['first_dt_ytd'].isin(week_dates_24)]
        matrix_table = self.prod_df_24_17.groupby(['recency','frequency'])['hshld'].nunique().unstack().sort_values(by='recency', ascending=True).reset_index()
        matrix_table = matrix_table.reindex(new_order)
        matrix_table.set_index('recency', inplace=True)
        self.weekly_metric_2024 = matrix_table['1x'].sum()
        self.weekly_metric_2024_5x = matrix_table['5x+'].sum()

        self.prod_df_24_18 = self.prod_df[self.prod_df['first_dt_ytd'].isin(week_dates_24_mod)]
        matrix_table_ = self.prod_df_24_18.groupby(['recency','frequency'])['hshld'].nunique().unstack().sort_values(by='recency', ascending=True).reset_index()
        matrix_table_ = matrix_table_.reindex(new_order)
        matrix_table_.set_index('recency', inplace=True)
        self.shifted_weekly_metric_2024 = matrix_table_['1x'].sum()
        self.shifted_weekly_metric_2024_5x = matrix_table_['5x+'].sum()

        self.weekly_margin_24 = round((self.margin_df_24['weekly_margin'].squeeze() / 1000000), 2)
        self.shifted_weekly_margin_24 = round((self.margin_df_24_['weekly_margin'].squeeze() / 1000000), 2)
        self.weekly_margin_23 = round((self.margin_df_23['weekly_margin'].squeeze() / 1000000), 2)
        self.shifted_weekly_margin_23 = round((self.margin_df_23_['weekly_margin'].squeeze() / 1000000), 2)
        self.weekly_ntb_demand_2024 = round((self.ntb_this_week['weekly_demand'].squeeze() / 1000), 1)
        self.shifted_weekly_ntb_demand_2024 = round((self.ntb_this_week_['weekly_demand'].squeeze() / 1000), 1)
        self.weekly_ntb_demand_2023 = round((self.ntb_this_week_ly['weekly_demand'].squeeze() / 1000), 1)
        self.shifted_weekly_ntb_demand_2023 = round((self.ntb_this_week_ly_['weekly_demand'].squeeze() / 1000), 1)
        
        self.ntb_acquisition_this_week = self.ntb_acquisition_this_week['weekly_ntb_acquisition'].squeeze()
        self.ntb_acquisition_this_week_ly = self.ntb_acquisition_this_week_ly['weekly_ntb_acquisition_ly'].squeeze()
        self.ntb_acquisition_shifted_week = self.ntb_acquisition_shifted_week['ntb_acquisition'].squeeze()
        self.ntb_acquisition_shifted_week_ly = self.ntb_acquisition_shifted_week_ly['ntb_acquisition'].squeeze()

        self.reactivated_acquisition_this_week = self.reactivated_acquisition_this_week['reactivated_count_fscl_wk'].squeeze()
        self.reactivated_acquisition_this_week_ly = self.reactivated_acquisition_this_week_ly['reactivated_count_fscl_wk'].squeeze()
        self.reactivated_acquisition_shifted_week = self.reactivated_acquisition_shifted_week['reactivated_count_fscl_wk'].squeeze()
        self.reactivated_acquisition_shifted_week_ly = self.reactivated_acquisition_shifted_week_ly['reactivated_count_fscl_wk'].squeeze()

    def construct_message(self):
        message = f"""\
        <html>
        <body>
    
            <p><strong>Fiscal Week Metrics :</strong></p>
            
            </p>Week {Fiscal_Week} 2024 [1x>2x]: {self.weekly_metric_2024}</p>
            </p>Week {Fiscal_Week} 2023 [1x>2x]: {self.weekly_metric_2023}</p>
            
            </p>Week {Fiscal_Week} 2024[5x+]: {self.weekly_metric_2024_5x}</p>
            </p>Week {Fiscal_Week} 2023[5x+]: {self.weekly_metric_2023_5x}</p>
            
            </p>Margin on Demand Week {Fiscal_Week}: {self.weekly_margin_24}M</p>
            </p>Margin on Demand Week {Fiscal_Week} LY: {self.weekly_margin_23}M</p>
    
            </p>NTB Acquisition 2024 Week {Fiscal_Week} : {self.ntb_acquisition_this_week}</p>
            </p>NTB Acquisition 2023 Week {Fiscal_Week} : {self.ntb_acquisition_this_week_ly}</p>
            
            </p>Reactivated Acquisition  2024 Week {Fiscal_Week} : {self.reactivated_acquisition_this_week}</p>
            </p>Reactivated Acquisition  2023 Week {Fiscal_Week} : {self.reactivated_acquisition_this_week_ly}</p>
            
            </p>Rolling 3 months NTB Demand TY: {self.weekly_ntb_demand_2024}K</p>
            </p>Rolling 3 months NTB Demand LY: {self.weekly_ntb_demand_2023}K</p>
    
            
            <p><strong>Shifted Week Metrics (Mon-Sun):</strong></p>
            
            </p>Shifted Week {Fiscal_Week} 2024[1x>2x]: {self.shifted_weekly_metric_2024}</p>
            </p>Shifted Week {Fiscal_Week} 2023[1x>2x]: {self.shifted_weekly_metric_2023}</p>
            
            </p>Shifted Week {Fiscal_Week} 2024[5x+]: {self.shifted_weekly_metric_2024_5x}</p>
            </p>Shifted Week {Fiscal_Week} 2023[5x+]: {self.shifted_weekly_metric_2023_5x}</p>
            
            </p>Margin on Demand Shifted Week {Fiscal_Week} : {self.shifted_weekly_margin_24}M</p>
            </p>Margin on Demand Shifted Week {Fiscal_Week} LY: {self.shifted_weekly_margin_23}M</p>
    
            </p>NTB Acquisition 2024 Shifted Week {Fiscal_Week} : {self.ntb_acquisition_shifted_week}</p>
            </p>NTB Acquisition 2023 Shifted  Week {Fiscal_Week} : {self.ntb_acquisition_shifted_week_ly}</p>
            
            </p>Reactivated Acquisition 2024 Shifted Week {Fiscal_Week} : {self.reactivated_acquisition_shifted_week}</p>
            </p>Reactivated Acquisition 2023 Shifted Week {Fiscal_Week} : {self.reactivated_acquisition_shifted_week_ly}</p>
            
            </p>Rolling 3 months NTB Demand Shifted Week TY: {self.shifted_weekly_ntb_demand_2024}K</p>
            </p>Rolling 3 months NTB Demand Shifted Week LY: {self.shifted_weekly_ntb_demand_2023}K</p>
            
            <p><strong>Email sent on {self.current_date}</strong></p>
            
        </body>
        </html>
        """
        return message

    def send_email(self, message):
        email_sender = EmailSender(self.sender_email, self.password)
        email_sender.send_email(self.receiver_email, message)

    def run(self):
        self.run_queries()
        self.calculate_metrics()
        message = self.construct_message()
        self.send_email(message)
        print("Script run complete, metrics updated and email sent.")


