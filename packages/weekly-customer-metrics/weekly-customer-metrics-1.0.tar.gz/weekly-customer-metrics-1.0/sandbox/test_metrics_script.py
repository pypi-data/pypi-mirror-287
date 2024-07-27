import pandas as pd
import datetime
import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.insert(0, r'C:\Users\nmdeshi\weekly_customer_metrics\datafeeds\db')
from redshift import *
from email_sender import *
from sql_queries import *

############################################################# Weekly Metrics ####################################################################################
print ( " Running queries to get weekly metrics data " )
prod_df = pd.read_sql_query( UAT_QUERY_3, prod_conn)
prod_df_23 = pd.read_sql_query( UAT_QUERY_4, prod_conn)

#2023 1x>2x Metric 
prod_df_23['first_dt_ytd'] = pd.to_datetime(prod_df_23['first_dt_ytd'])
prod_df_23_16= prod_df_23[prod_df_23['first_dt_ytd'].isin(week_dates_23)]

matrix_table_23= prod_df_23_16.groupby(['recency','frequency'])['hshld'].nunique().unstack().sort_values(by='recency', ascending=True).reset_index()
new_order = [0,4,1,2,3]

matrix_table_23 = matrix_table_23.reindex(new_order)
matrix_table_23.set_index('recency',inplace=True)

weekly_metric_2023 = matrix_table_23['1x'].sum()
weekly_metric_2023_5x = matrix_table_23['5x+'].sum()


# 2023 1x>2x metric shifted Week ( Mon- Sun )
prod_df_23_17= prod_df_23[prod_df_23['first_dt_ytd'].isin(week_dates_23_mod)]
matrix_table_23_= prod_df_23_17.groupby(['recency','frequency'])['hshld'].nunique().unstack().sort_values(by='recency', ascending=True).reset_index()
new_order = [0,4,1,2,3]
matrix_table_23_ = matrix_table_23_.reindex(new_order)
matrix_table_23_.set_index('recency',inplace=True)
shifted_weekly_metric_2023 = matrix_table_23_['1x'].sum()
shifted_weekly_metric_2023_5x = matrix_table_23_['5x+'].sum()


#2024 1x>2x Metric
prod_df['first_dt_ytd'] = pd.to_datetime(prod_df['first_dt_ytd'])
prod_df_24_17= prod_df [prod_df['first_dt_ytd'].isin(week_dates_24)]
matrix_table= prod_df_24_17.groupby(['recency','frequency'])['hshld'].nunique().unstack().sort_values(by='recency', ascending=True).reset_index()
new_order = [0,4,1,2,3]
matrix_table = matrix_table.reindex(new_order)
matrix_table.set_index('recency',inplace=True)
weekly_metric_2024 = matrix_table['1x'].sum()
weekly_metric_2024_5x = matrix_table['5x+'].sum()


# 2024 1x>2x metric shifted Week ( Mon- Sun )
prod_df_24_18= prod_df [prod_df['first_dt_ytd'].isin(week_dates_24_mod)]
matrix_table_= prod_df_24_18.groupby(['recency','frequency'])['hshld'].nunique().unstack().sort_values(by='recency', ascending=True).reset_index()
new_order = [0,4,1,2,3]
matrix_table_ = matrix_table_.reindex(new_order)
matrix_table_.set_index('recency',inplace=True)
shifted_weekly_metric_2024 = matrix_table_['1x'].sum()
shifted_weekly_metric_2024_5x = matrix_table_['5x+'].sum()


#2024 Margin on Demand
margin_df_24 =pd.read_sql_query(UAT_QUERY_5 , prod_conn) 
weekly_margin_24 = margin_df_24['weekly_margin'].squeeze()
weekly_margin_24= round((weekly_margin_24/1000000),2)


#2024 Margin on Demand Shifted Week
margin_df_24_ = pd.read_sql_query(UAT_QUERY_6 , prod_conn) 
shifted_weekly_margin_24 = margin_df_24_['weekly_margin'].squeeze()
shifted_weekly_margin_24= round((shifted_weekly_margin_24/1000000),2)


#2023 Margin on Demand
margin_df_23 = pd.read_sql_query(UAT_QUERY_7 , prod_conn)
weekly_margin_23 = margin_df_23['weekly_margin'].squeeze()
weekly_margin_23= round((weekly_margin_23/1000000),2)

#2023 Margin on Demand Shifted Week
margin_df_23_ = pd.read_sql_query(UAT_QUERY_8 , prod_conn)
shifted_weekly_margin_23 = margin_df_23_['weekly_margin'].squeeze()
shifted_weekly_margin_23= round((shifted_weekly_margin_23/1000000),2)


# 2024 Acqusition Performance 
ntb_this_week = pd.read_sql_query(UAT_QUERY_9 , prod_conn)
weekly_ntb_demand_2024 = ntb_this_week['weekly_demand'].squeeze()
weekly_ntb_demand_2024 = round((weekly_ntb_demand_2024/1000),1)

# 2024 Acqusition Performance Shifted Week
ntb_this_week_ = pd.read_sql_query(UAT_QUERY_10 , prod_conn)
shifted_weekly_ntb_demand_2024 = ntb_this_week_['weekly_demand'].squeeze()
shifted_weekly_ntb_demand_2024 = round((shifted_weekly_ntb_demand_2024/1000),1)

# 2023 Acqusition Performance 
ntb_this_week_ly = pd.read_sql_query(UAT_QUERY_11 , prod_conn)
weekly_ntb_demand_2023 = ntb_this_week_ly['weekly_demand'].squeeze()
weekly_ntb_demand_2023 = round((weekly_ntb_demand_2023/1000),1)


# 2023 Acqusition Performance Shifted Week
ntb_this_week_ly_ =  pd.read_sql_query(UAT_QUERY_12 , prod_conn)
shifted_weekly_ntb_demand_2023 = ntb_this_week_ly_['weekly_demand'].squeeze()
shifted_weekly_ntb_demand_2023 = round((shifted_weekly_ntb_demand_2023/1000),1)

print(" Script Run Complete, Metrics Updated ")

message = f"""\
Subject: Email for Weekly Customer Metrics 

Fiscal Week Metrics : 

Week {Fiscal_Week} 2024[1x>2x]: {weekly_metric_2024}
Week {Fiscal_Week} 2023[1x>2x] :{weekly_metric_2023}

Week {Fiscal_Week} 2024[5x+]: {weekly_metric_2024_5x}
Week {Fiscal_Week} 2023[5x+]:{weekly_metric_2023_5x}


Margin on Demand Week {Fiscal_Week}  : {weekly_margin_24}M
Margin on Demand Week {Fiscal_Week} LY : {weekly_margin_23}M

Rolling 3 months NTB Demand TY : {weekly_ntb_demand_2024}K
Rollling 3 months NTB Demand LY : {weekly_ntb_demand_2023}K



Shifted Week Metrics(Mon-Sun):

Shifted Week {Fiscal_Week} 2024[1x>2x]: {shifted_weekly_metric_2024}
Shifted Week {Fiscal_Week} 2023[1x>2x]: {shifted_weekly_metric_2023}

Shifted Week {Fiscal_Week} 2024[5x+]: {shifted_weekly_metric_2024_5x}
Shifted Week {Fiscal_Week} 2023[5x+]: {shifted_weekly_metric_2023_5x}


Margin on Demand Shifted Week :    {shifted_weekly_margin_24}M
Margin on Demand Shifted Week LY : {shifted_weekly_margin_23}M

Rolling 3 months NTB Demand Shifted Week TY :  {shifted_weekly_ntb_demand_2024}K
Rollling 3 months NTB Demand Shifted Week LY : {shifted_weekly_ntb_demand_2023}K


Email sent on '{current_date}'

"""

print( " Sending Email ")

 # Sending EMAIL 
email_sender = EmailSender(SENDER_EMAIL, PASSWORD)
email_sender.send_email(RECEIVER_EMAIL, message)



