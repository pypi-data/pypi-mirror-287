import pandas as pd
import datetime

def get_fscl_yr_wk(prod_conn):
    current_date = datetime.date.today().strftime('%Y-%m-%d')

    query = f"""
    select fscl_yr_wk
    from lehub.fscl_cal_dt fcd 
    where fscl_yr = 2024
    and fscl_cal_num = 4
    and cal_dt = '{current_date}'
    """
    
    # Execute the query
    test_df = pd.read_sql_query(query, prod_conn)
    
    
    if not test_df.empty:
        # Extract the value from the DataFrame
        fscl_yr_wk = test_df['fscl_yr_wk'].iloc[0]
        
        # Subtract 1 from the value
        fscl_yr_wk_minus_1 = fscl_yr_wk - 1
        
        return fscl_yr_wk_minus_1
    else:
        raise ValueError("The query did not return any results.")


def calculate_dates():
    current_date = datetime.date.today()
    
    # Calculate 1 day before the current date
    one_day_before = current_date - datetime.timedelta(days=1)
    one_day_before_ly = one_day_before - datetime.timedelta(days=366)

    # Calculate 3 months (approximately 99 days) before the current date
    three_months_before = current_date - datetime.timedelta(days=99)
    three_months_before_ly = one_day_before_ly - datetime.timedelta(days=99)

    # Convert the dates to the required format (YYYY-MM-DD)
    date_string = one_day_before.strftime('%Y-%m-%d')
    date_string_ly = one_day_before_ly.strftime('%Y-%m-%d')
    date_string_3_months_before = three_months_before.strftime('%Y-%m-%d')
    date_string_3_months_before_ly = three_months_before_ly.strftime('%Y-%m-%d')

    return date_string, date_string_ly, date_string_3_months_before, date_string_3_months_before_ly