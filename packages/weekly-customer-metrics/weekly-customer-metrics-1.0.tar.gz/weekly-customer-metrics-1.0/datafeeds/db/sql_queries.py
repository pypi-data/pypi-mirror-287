## Set Fiscal Week 
import datetime 
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.insert(0, r'C:\Users\nmdeshi\weekly_customer_metrics\datafeeds\db')
from redshift import *
from helpers import *

# Set Fiscal Week  
Fiscal_Week =  get_fscl_yr_wk(prod_conn)
print(f" Updating SQL Queries for Week {Fiscal_Week} ")

# Get Dates for below queries
date_string, date_string_ly, date_string_3_months_before, date_string_3_months_before_ly = calculate_dates()


############### Fiscal Week Date Queries #####################################
UAT_QUERY = f"""
select  fscl_yr,  cal_dt , fscl_yr_wk 
from lehub.fscl_cal_dt fcd 
where fscl_yr =2024
and fscl_cal_num = 4
and fscl_yr_wk = {Fiscal_Week}
order by cal_dt ASC
"""

UAT_QUERY_2 = f"""
select  fscl_yr,  cal_dt , fscl_yr_wk 
from lehub.fscl_cal_dt fcd 
where fscl_yr =2023
and fscl_cal_num = 4
and fscl_yr_wk = {Fiscal_Week}
order by cal_dt ASC
"""
############################### 2024 ########################################
dates_24 = pd.read_sql_query( UAT_QUERY, prod_conn)
week_dates_24= dates_24['cal_dt'].tolist()

min_date_24 = dates_24['cal_dt'].min().strftime('%Y-%m-%d')
max_date_24 = dates_24['cal_dt'].max().strftime('%Y-%m-%d')

# Shifted Week Dates ( Mon- Sun )
dates_24['cal_dt_mod'] = dates_24['cal_dt'] + pd.Timedelta(days=2)

week_dates_24_mod= dates_24['cal_dt_mod'].tolist()

min_date_24_shifted = dates_24['cal_dt_mod'].min().strftime('%Y-%m-%d')
max_date_24_shifted = dates_24['cal_dt_mod'].max().strftime('%Y-%m-%d')

########################### 2023 #############################################
dates_23 = pd.read_sql_query( UAT_QUERY_2 , prod_conn) 
week_dates_23= dates_23['cal_dt'].tolist()
min_date_23 = dates_23['cal_dt'].min().strftime('%Y-%m-%d')
max_date_23 = dates_23['cal_dt'].max().strftime('%Y-%m-%d')


#Shifted Week Dates ( Mon- Sun )

dates_23['cal_dt_mod'] = dates_23['cal_dt'] + pd.Timedelta(days=2)

week_dates_23_mod= dates_23['cal_dt_mod'].tolist()

min_date_23_shifted = dates_23['cal_dt_mod'].min().strftime('%Y-%m-%d')
max_date_23_shifted = dates_23['cal_dt_mod'].max().strftime('%Y-%m-%d')


#########################  Weekly Metric queries ###################################################

UAT_QUERY_3 = f"""with FirstPurchaseRecencyfreq as (
 select
    vc.edw_hshld_num as hshld,
    max(fdi.src_ord_dt) as lp_before_2023,count(distinct fdi.src_ord_dt||fdi.src_ord_num) as orders,datediff(months , lp_before_2023 , '2024-02-02') as months_between,
    case when months_between between 0 and 6  then '0-6M'
	 when months_between between 7 and 12 then '7-12M'
	 when months_between between 13 and 24 then '13-24M'
	 when months_between between 25 and 36 then '25-36M'
  when months_between between 37 and 60 then '37-60M'
  when months_between > 60 then '60M+'
end as recency, case when orders = 1 then '1x'
	 when orders = 2 then '2x'
	 when orders = 3  then '3x'
      when orders = 4 then '4x'
      when orders > 4 then '5x+'
	 end as frequency
  from
    lehub.vw_consumer as vc
    join lehub.FCT_DMD_ITEM as fdi
      on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM
    join lehub.sku as sk
    on fdi.sku_num = sk.sku_num 
  where fdi.bus_unit_num = 1
    and fdi.alt_bus_unit_num in (1,2)
    and fdi.reg_dmd_qty > 0
    and fdi.dmd_amt > 0
    and fdi.schl_id is null 
    and fdi.src_ord_dt between '2019-02-02' and '2024-02-02'
  group by 
    vc.edw_hshld_num
),

quarter_1_2023 as (
select FirstPurchaseRecencyfreq.hshld as hshld_num , count(distinct fdi.src_ord_dt||fdi.src_ord_num) as orders_2023_q1 , sum(nvl(fdi.dmd_amt,0)) as demand,  min(fdi.src_ord_dt) as first_dt_ytd 
from FirstPurchaseRecencyfreq join lehub.vw_consumer as vc 
    on vc.edw_hshld_num = FirstPurchaseRecencyfreq.hshld 
join lehub.FCT_DMD_ITEM as fdi
on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM
join lehub.sku as sk
    on fdi.sku_num = sk.sku_num 
 join lehub.ISS_COMP IC
		on ic.iss_comp_num = fdi.iss_comp_num
join lehub.fscl_cal_dt                as fcd
	on fdi.src_ord_dt  = fcd.cal_dt   
left join lehub.fct_ship_item                      as fsi
	on fdi.src_ord_dt   = fsi.src_ord_dt   and
 	fdi.src_ord_num  = fsi.src_ord_num  and
 	fdi.item_seq_num = fsi.item_seq_num and
 	fdi.bus_unit_num = fsi.bus_unit_num
 where fdi.bus_unit_num = 1
   and fdi.alt_bus_unit_num in (1,2)
   and fdi.reg_dmd_qty > 0
   and fdi.dmd_amt > 0
   and fdi.schl_id is null 
   and fcd.fscl_cal_num   = 4
   and fcd.fscl_yr        = 2024
   and fdi.src_ord_dt between '2024-02-03' and '{date_string}'
   group by 1 
)

select * , case when quarter_1_2023.hshld_num is not null then 1 else 0 end as purchased_in_q1_23
from FirstPurchaseRecencyfreq
left join quarter_1_2023
on FirstPurchaseRecencyfreq.hshld = quarter_1_2023.hshld_num

  
"""

UAT_QUERY_4 = f"""with FirstPurchaseRecencyfreq as (
 select
    vc.edw_hshld_num as hshld,
    max(fdi.src_ord_dt) as lp_before_2023,count(distinct fdi.src_ord_dt||fdi.src_ord_num) as orders,datediff(months , lp_before_2023 , '2023-02-02') as months_between,
    case when months_between between 0 and 6  then '0-6M'
	 when months_between between 7 and 12 then '7-12M'
	 when months_between between 13 and 24 then '13-24M'
	 when months_between between 25 and 36 then '25-36M'
  when months_between between 37 and 60 then '37-60M'
  when months_between > 60 then '60M+'
end as recency, case when orders = 1 then '1x'
	 when orders = 2 then '2x'
	 when orders = 3  then '3x'
      when orders = 4 then '4x'
      when orders > 4 then '5x+'
	 end as frequency
  from
    lehub.vw_consumer as vc
    join lehub.FCT_DMD_ITEM as fdi
      on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM
    join lehub.sku as sk
    on fdi.sku_num = sk.sku_num 
  where fdi.bus_unit_num = 1
    and fdi.alt_bus_unit_num in (1,2)
    and fdi.reg_dmd_qty > 0
    and fdi.dmd_amt > 0
    and fdi.schl_id is null 
    and fdi.src_ord_dt between '2018-02-02' and '2023-02-02'
  group by 
    vc.edw_hshld_num
),

quarter_1_2023 as (
select FirstPurchaseRecencyfreq.hshld as hshld_num , count(distinct fdi.src_ord_dt||fdi.src_ord_num) as orders_2023_q1 , sum(nvl(fdi.dmd_amt,0)) as demand ,  min(fdi.src_ord_dt) as first_dt_ytd 
from FirstPurchaseRecencyfreq join lehub.vw_consumer as vc 
    on vc.edw_hshld_num = FirstPurchaseRecencyfreq.hshld 
join lehub.FCT_DMD_ITEM as fdi
on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM
join lehub.sku as sk
    on fdi.sku_num = sk.sku_num 
 join lehub.ISS_COMP IC
		on ic.iss_comp_num = fdi.iss_comp_num
join lehub.fscl_cal_dt                as fcd
	on fdi.src_ord_dt  = fcd.cal_dt   
left join lehub.fct_ship_item                      as fsi
	on fdi.src_ord_dt   = fsi.src_ord_dt   and
 	fdi.src_ord_num  = fsi.src_ord_num  and
 	fdi.item_seq_num = fsi.item_seq_num and
 	fdi.bus_unit_num = fsi.bus_unit_num
 where fdi.bus_unit_num = 1
   and fdi.alt_bus_unit_num in (1,2)
   and fdi.reg_dmd_qty > 0
   and fdi.dmd_amt > 0
   and fdi.schl_id is null 
   and fcd.fscl_cal_num   = 4
   and fcd.fscl_yr        = 2023 
   and fdi.src_ord_dt between '2023-02-03' and '{date_string_ly}'
   group by 1
)

select * , case when quarter_1_2023.hshld_num is not null then 1 else 0 end as purchased_in_q1_23
from FirstPurchaseRecencyfreq
left join quarter_1_2023
on FirstPurchaseRecencyfreq.hshld = quarter_1_2023.hshld_num
"""
UAT_QUERY_5 = f"""
select sum(margin) as weekly_margin from (
select vc.edw_hshld_num hshl ,fdi.dmd_amt dmd, fdi.cst_amt prod_price , dmd- prod_price as margin 
from lehub.VW_CONSUMER vc
inner join lehub.FCT_DMD_ITEM fdi
	on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
where fdi.REG_DMD_QTY > 0 
and fdi.BUS_UNIT_NUM = 1
and fdi.alt_bus_unit_num in (1,2)
and fdi.src_ord_dt between '{min_date_24}' and '{max_date_24}'
)
"""

UAT_QUERY_6 = f"""
select sum(margin) as weekly_margin from (
select vc.edw_hshld_num hshl ,fdi.dmd_amt dmd, fdi.cst_amt prod_price , dmd- prod_price as margin 
from lehub.VW_CONSUMER vc
inner join lehub.FCT_DMD_ITEM fdi
	on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
where fdi.REG_DMD_QTY > 0 
and fdi.BUS_UNIT_NUM = 1
and fdi.alt_bus_unit_num in (1,2)
and fdi.src_ord_dt between '{min_date_24_shifted}' and '{max_date_24_shifted}'
)
"""

UAT_QUERY_7 = f"""
select sum(margin) as weekly_margin from (
select vc.edw_hshld_num hshl ,fdi.dmd_amt dmd, fdi.cst_amt prod_price , dmd- prod_price as margin 
from lehub.VW_CONSUMER vc
inner join lehub.FCT_DMD_ITEM fdi
	on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
where fdi.REG_DMD_QTY > 0 
and fdi.BUS_UNIT_NUM = 1
and fdi.alt_bus_unit_num in (1,2)
and fdi.src_ord_dt between '{min_date_23}' and '{max_date_23}'
)
"""

UAT_QUERY_8 = f"""
select sum(margin) as weekly_margin from (
select vc.edw_hshld_num hshl ,fdi.dmd_amt dmd, fdi.cst_amt prod_price , dmd- prod_price as margin 
from lehub.VW_CONSUMER vc
inner join lehub.FCT_DMD_ITEM fdi
	on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
where fdi.REG_DMD_QTY > 0 
and fdi.BUS_UNIT_NUM = 1
and fdi.alt_bus_unit_num in (1,2)
and fdi.src_ord_dt between '{min_date_23_shifted}' and '{max_date_23_shifted}'
)
""" 

min_date_24_dt = datetime.datetime.strptime(min_date_24, '%Y-%m-%d')
min_date_24_minus_one = min_date_24_dt - datetime.timedelta(days=1)
min_date_24_minus_one_str = min_date_24_minus_one.strftime('%Y-%m-%d')

UAT_QUERY_9 = f"""
WITH NTB AS (
    SELECT vc.edw_hshld_num AS hshl, MIN(first_dt) AS first_purchase_dt  
    FROM lehub.VW_CONSUMER vc
    INNER JOIN lehub.FCT_DMD_ITEM fdi ON vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
    INNER JOIN lehub.sku sk ON fdi.sku_num = sk.sku_num
    INNER JOIN (
        SELECT hp.edw_hshld_num AS edw_hshld_num, hp.first_dt AS first_dt, H.chnl_cd AS chnl_cd 
        FROM (
            SELECT edw_hshld_num, MIN(ord_fr_act_dt) AS first_dt
            FROM lehub.HSHLD_PURCH_SUM H
            GROUP BY edw_hshld_num
        ) hp
        INNER JOIN lehub.HSHLD_PURCH_SUM H 
            ON hp.edw_hshld_num = H.edw_hshld_num AND hp.first_dt = H.ord_fr_act_dt
        INNER JOIN lehub.FSCL_CAL_DT fcd ON hp.first_dt = fcd.CAL_DT
        WHERE fcd.FSCL_CAL_NUM = 4 
        AND H.chnl_cd = 1
        AND fcd.cal_dt BETWEEN '{date_string_3_months_before}' AND '{min_date_24_minus_one_str}'
    ) HPS ON HPS.edw_hshld_num = vc.edw_hshld_num AND HPS.first_dt = fdi.src_ord_dt
    INNER JOIN lehub.FSCL_CAL_DT fcd ON fdi.SRC_ORD_DT = fcd.CAL_DT
    WHERE fdi.REG_DMD_QTY > 0 
    AND fdi.BUS_UNIT_NUM = 1
    AND fcd.FSCL_CAL_NUM = 4 
    AND fdi.src_ord_dt BETWEEN '{date_string_3_months_before}' AND '{min_date_24_minus_one_str}'
    AND fdi.alt_bus_unit_num IN (1, 2)
    GROUP BY vc.edw_hshld_num
)
SELECT SUM(fdi.dmd_amt) AS weekly_demand
FROM NTB 
JOIN lehub.VW_CONSUMER vc ON NTB.hshl = vc.edw_hshld_num 
JOIN lehub.FCT_DMD_ITEM fdi ON vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
JOIN lehub.FSCL_CAL_DT fcd ON fdi.SRC_ORD_DT = fcd.CAL_DT
WHERE fdi.REG_DMD_QTY > 0 
AND fdi.BUS_UNIT_NUM = 1
AND fdi.alt_bus_unit_num IN (1, 2)
AND fcd.FSCL_CAL_NUM = 4 	
AND fcd.fscl_yr = 2024
AND fcd.fscl_yr_wk = {Fiscal_Week}
""" 

min_date_24_dt = datetime.datetime.strptime(min_date_24_shifted, '%Y-%m-%d')
min_date_24_shifted_minus_one = min_date_24_dt - datetime.timedelta(days=1)
min_date_24_minus_one_str = min_date_24_minus_one.strftime('%Y-%m-%d')

UAT_QUERY_10 = f"""
WITH NTB AS (
    SELECT vc.edw_hshld_num AS hshl, MIN(first_dt) AS first_purchase_dt  
    FROM lehub.VW_CONSUMER vc
    INNER JOIN lehub.FCT_DMD_ITEM fdi ON vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
    INNER JOIN lehub.sku sk ON fdi.sku_num = sk.sku_num
    INNER JOIN (
        SELECT hp.edw_hshld_num AS edw_hshld_num, hp.first_dt AS first_dt, H.chnl_cd AS chnl_cd 
        FROM (
            SELECT edw_hshld_num, MIN(ord_fr_act_dt) AS first_dt
            FROM lehub.HSHLD_PURCH_SUM H
            GROUP BY edw_hshld_num
        ) hp
        INNER JOIN lehub.HSHLD_PURCH_SUM H 
            ON hp.edw_hshld_num = H.edw_hshld_num AND hp.first_dt = H.ord_fr_act_dt
        INNER JOIN lehub.FSCL_CAL_DT fcd ON hp.first_dt = fcd.CAL_DT
        WHERE fcd.FSCL_CAL_NUM = 4 
        AND H.chnl_cd = 1
        AND fcd.cal_dt BETWEEN '{date_string_3_months_before}' AND '{min_date_24_shifted_minus_one}'
    ) HPS ON HPS.edw_hshld_num = vc.edw_hshld_num AND HPS.first_dt = fdi.src_ord_dt
    INNER JOIN lehub.FSCL_CAL_DT fcd ON fdi.SRC_ORD_DT = fcd.CAL_DT
    WHERE fdi.REG_DMD_QTY > 0 
    AND fdi.BUS_UNIT_NUM = 1
    AND fcd.FSCL_CAL_NUM = 4 
    AND fdi.src_ord_dt BETWEEN '{date_string_3_months_before}' AND '{min_date_24_shifted_minus_one}'
    AND fdi.alt_bus_unit_num IN (1, 2)
    GROUP BY vc.edw_hshld_num
)
SELECT SUM(fdi.dmd_amt) AS weekly_demand
FROM NTB 
JOIN lehub.VW_CONSUMER vc ON NTB.hshl = vc.edw_hshld_num 
JOIN lehub.FCT_DMD_ITEM fdi ON vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
JOIN lehub.FSCL_CAL_DT fcd ON fdi.SRC_ORD_DT = fcd.CAL_DT
WHERE fdi.REG_DMD_QTY > 0 
AND fdi.BUS_UNIT_NUM = 1
AND fdi.alt_bus_unit_num IN (1, 2)
AND fcd.FSCL_CAL_NUM = 4 	
AND fcd.fscl_yr = 2024
AND fcd.cal_dt BETWEEN '{min_date_24_shifted}' AND '{max_date_24_shifted}'
"""

min_date_23_dt = datetime.datetime.strptime(min_date_23, '%Y-%m-%d')
min_date_23_minus_one = min_date_23_dt - datetime.timedelta(days=1)
min_date_23_minus_one_str = min_date_23_minus_one.strftime('%Y-%m-%d')

UAT_QUERY_11 = f"""
WITH NTB AS (
    SELECT vc.edw_hshld_num AS hshl, MIN(first_dt) AS first_purchase_dt  
    FROM lehub.VW_CONSUMER vc
    INNER JOIN lehub.FCT_DMD_ITEM fdi ON vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
    INNER JOIN lehub.sku sk ON fdi.sku_num = sk.sku_num
    INNER JOIN (
        SELECT hp.edw_hshld_num AS edw_hshld_num, hp.first_dt AS first_dt, H.chnl_cd AS chnl_cd 
        FROM (
            SELECT edw_hshld_num, MIN(ord_fr_act_dt) AS first_dt
            FROM lehub.HSHLD_PURCH_SUM H
            GROUP BY edw_hshld_num
        ) hp
        INNER JOIN lehub.HSHLD_PURCH_SUM H 
            ON hp.edw_hshld_num = H.edw_hshld_num AND hp.first_dt = H.ord_fr_act_dt
        INNER JOIN lehub.FSCL_CAL_DT fcd ON hp.first_dt = fcd.CAL_DT
        WHERE fcd.FSCL_CAL_NUM = 4 
        AND H.chnl_cd = 1
        AND fcd.cal_dt BETWEEN '{date_string_3_months_before_ly}' AND '{min_date_23_minus_one_str}'
    ) HPS ON HPS.edw_hshld_num = vc.edw_hshld_num AND HPS.first_dt = fdi.src_ord_dt
    INNER JOIN lehub.FSCL_CAL_DT fcd ON fdi.SRC_ORD_DT = fcd.CAL_DT
    WHERE fdi.REG_DMD_QTY > 0 
    AND fdi.BUS_UNIT_NUM = 1
    AND fcd.FSCL_CAL_NUM = 4 
    AND fdi.src_ord_dt BETWEEN '{date_string_3_months_before_ly}' AND '{min_date_23_minus_one_str}'
    AND fdi.alt_bus_unit_num IN (1, 2)
    GROUP BY vc.edw_hshld_num
)
SELECT SUM(fdi.dmd_amt) AS weekly_demand
FROM NTB 
JOIN lehub.VW_CONSUMER vc ON NTB.hshl = vc.edw_hshld_num 
JOIN lehub.FCT_DMD_ITEM fdi ON vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
JOIN lehub.FSCL_CAL_DT fcd ON fdi.SRC_ORD_DT = fcd.CAL_DT
WHERE fdi.REG_DMD_QTY > 0 
AND fdi.BUS_UNIT_NUM = 1
AND fdi.alt_bus_unit_num IN (1, 2)
AND fcd.FSCL_CAL_NUM = 4 	
AND fcd.fscl_yr = 2023
AND fcd.fscl_yr_wk = {Fiscal_Week}
"""


min_date_23_dt = datetime.datetime.strptime(min_date_23_shifted, '%Y-%m-%d')
min_date_23_minus_one = min_date_23_dt - datetime.timedelta(days=1)
min_date_23_shifted_minus_one_str = min_date_23_minus_one.strftime('%Y-%m-%d')

UAT_QUERY_12 = f"""
WITH NTB AS (
    SELECT vc.edw_hshld_num AS hshl, MIN(first_dt) AS first_purchase_dt  
    FROM lehub.VW_CONSUMER vc
    INNER JOIN lehub.FCT_DMD_ITEM fdi ON vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
    INNER JOIN lehub.sku sk ON fdi.sku_num = sk.sku_num
    INNER JOIN (
        SELECT hp.edw_hshld_num AS edw_hshld_num, hp.first_dt AS first_dt, H.chnl_cd AS chnl_cd 
        FROM (
            SELECT edw_hshld_num, MIN(ord_fr_act_dt) AS first_dt
            FROM lehub.HSHLD_PURCH_SUM H
            GROUP BY edw_hshld_num
        ) hp
        INNER JOIN lehub.HSHLD_PURCH_SUM H 
            ON hp.edw_hshld_num = H.edw_hshld_num AND hp.first_dt = H.ord_fr_act_dt
        INNER JOIN lehub.FSCL_CAL_DT fcd ON hp.first_dt = fcd.CAL_DT
        WHERE fcd.FSCL_CAL_NUM = 4 
        AND H.chnl_cd = 1
        AND fcd.cal_dt BETWEEN '{date_string_3_months_before_ly}' AND '{min_date_23_shifted_minus_one_str}'
    ) HPS ON HPS.edw_hshld_num = vc.edw_hshld_num AND HPS.first_dt = fdi.src_ord_dt
    INNER JOIN lehub.FSCL_CAL_DT fcd ON fdi.SRC_ORD_DT = fcd.CAL_DT
    WHERE fdi.REG_DMD_QTY > 0 
    AND fdi.BUS_UNIT_NUM = 1
    AND fcd.FSCL_CAL_NUM = 4 
    AND fdi.src_ord_dt BETWEEN '{date_string_3_months_before_ly}' AND '{min_date_23_shifted_minus_one_str}'
    AND fdi.alt_bus_unit_num IN (1, 2)
    GROUP BY vc.edw_hshld_num
)
SELECT SUM(fdi.dmd_amt) AS weekly_demand
FROM NTB 
JOIN lehub.VW_CONSUMER vc ON NTB.hshl = vc.edw_hshld_num 
JOIN lehub.FCT_DMD_ITEM fdi ON vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
JOIN lehub.FSCL_CAL_DT fcd ON fdi.SRC_ORD_DT = fcd.CAL_DT
WHERE fdi.REG_DMD_QTY > 0 
AND fdi.BUS_UNIT_NUM = 1
AND fdi.alt_bus_unit_num IN (1, 2)
AND fcd.FSCL_CAL_NUM = 4 	
AND fcd.fscl_yr = 2023
AND fcd.cal_dt BETWEEN '{min_date_23_shifted}' AND '{max_date_23_shifted}'
"""

UAT_QUERY_13 = f"""
select count(distinct hshl) as weekly_ntb_acquisition from 
(select vc.edw_hshld_num hshl ,min(first_dt) as first_purchase_dt 
from lehub.VW_CONSUMER vc
inner join lehub.FCT_DMD_ITEM fdi
	on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
inner join lehub.sku sk 
on fdi.sku_num = sk.sku_num
inner join
(select hp.edw_hshld_num edw_hshld_num, hp.first_dt first_dt, H.chnl_cd chnl_cd from
		(
		select edw_hshld_num, min(ord_fr_act_dt) as first_dt
    	from lehub.HSHLD_PURCH_SUM H
    	group by 1
		)hp
		inner join lehub.HSHLD_PURCH_SUM H 
			on hp.edw_hshld_num = H.edw_hshld_num
			and hp.first_dt = H.ord_fr_act_dt
		inner join lehub.FSCL_CAL_DT fcd
			on hp.first_dt = fcd.CAL_DT	
		where fcd.FSCL_CAL_NUM = 4 
		and H.chnl_cd = 1
		and fcd.fscl_yr = 2024
		and fcd.fscl_yr_wk = {Fiscal_Week}
		
)HPS
on HPS.edw_hshld_num = VC.edw_hshld_num and HPS.first_dt = fdi.src_ord_dt
inner join lehub.FSCL_CAL_DT fcd
	on fdi.SRC_ORD_DT = fcd.CAL_DT
where fdi.REG_DMD_QTY > 0 
and fdi.BUS_UNIT_NUM = 1
and fcd.FSCL_CAL_NUM = 4 
and fcd.fscl_yr = 2024
and fcd.fscl_yr_wk = {Fiscal_Week}
and fdi.alt_bus_unit_num in (1,2)
group by 1
)
"""

UAT_QUERY_14 = f"""
select count(distinct hshl) as weekly_ntb_acquisition_ly from 
(select vc.edw_hshld_num hshl ,min(first_dt) as first_purchase_dt 
from lehub.VW_CONSUMER vc
inner join lehub.FCT_DMD_ITEM fdi
	on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
inner join lehub.sku sk 
on fdi.sku_num = sk.sku_num
inner join
(select hp.edw_hshld_num edw_hshld_num, hp.first_dt first_dt, H.chnl_cd chnl_cd from
		(
		select edw_hshld_num, min(ord_fr_act_dt) as first_dt
    	from lehub.HSHLD_PURCH_SUM H
    	group by 1
		)hp
		inner join lehub.HSHLD_PURCH_SUM H 
			on hp.edw_hshld_num = H.edw_hshld_num
			and hp.first_dt = H.ord_fr_act_dt
		inner join lehub.FSCL_CAL_DT fcd
			on hp.first_dt = fcd.CAL_DT	
		where fcd.FSCL_CAL_NUM = 4 
		and H.chnl_cd = 1
		and fcd.fscl_yr = 2023
		and fcd.fscl_yr_wk = {Fiscal_Week}
		
)HPS
on HPS.edw_hshld_num = VC.edw_hshld_num and HPS.first_dt = fdi.src_ord_dt
inner join lehub.FSCL_CAL_DT fcd
	on fdi.SRC_ORD_DT = fcd.CAL_DT
where fdi.REG_DMD_QTY > 0 
and fdi.BUS_UNIT_NUM = 1
and fcd.FSCL_CAL_NUM = 4 
and fcd.fscl_yr = 2023
and fcd.fscl_yr_wk = {Fiscal_Week}
and fdi.alt_bus_unit_num in (1,2)
group by 1
)
"""

UAT_QUERY_15 = f"""
select count(distinct hshl) as ntb_acquisition from (
select vc.edw_hshld_num hshl ,min(first_dt) as first_purchase_dt 
from lehub.VW_CONSUMER vc
inner join lehub.FCT_DMD_ITEM fdi
	on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
inner join lehub.sku sk 
on fdi.sku_num = sk.sku_num
inner join
(select hp.edw_hshld_num edw_hshld_num, hp.first_dt first_dt, H.chnl_cd chnl_cd from
		(
		select edw_hshld_num, min(ord_fr_act_dt) as first_dt
    	from lehub.HSHLD_PURCH_SUM H
    	group by 1
		)hp
		inner join lehub.HSHLD_PURCH_SUM H 
			on hp.edw_hshld_num = H.edw_hshld_num
			and hp.first_dt = H.ord_fr_act_dt
		inner join lehub.FSCL_CAL_DT fcd
			on hp.first_dt = fcd.CAL_DT	
		where fcd.FSCL_CAL_NUM = 4 
		and H.chnl_cd = 1
		and fcd.fscl_yr = 2024
		and fcd.cal_dt between '{min_date_24_shifted}' AND '{max_date_24_shifted}'
		
)HPS
on HPS.edw_hshld_num = VC.edw_hshld_num and HPS.first_dt = fdi.src_ord_dt
inner join lehub.FSCL_CAL_DT fcd
	on fdi.SRC_ORD_DT = fcd.CAL_DT
where fdi.REG_DMD_QTY > 0 
and fdi.BUS_UNIT_NUM = 1
and fcd.FSCL_CAL_NUM = 4 
and fcd.fscl_yr = 2024
and fdi.src_ord_dt between '{min_date_24_shifted}' AND '{max_date_24_shifted}'
and fdi.alt_bus_unit_num in (1,2)
group by 1
)
"""

UAT_QUERY_16 = f"""
select count(distinct hshl) ntb_acquisition from (
select vc.edw_hshld_num hshl ,min(first_dt) as first_purchase_dt 
from lehub.VW_CONSUMER vc
inner join lehub.FCT_DMD_ITEM fdi
	on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM 
inner join lehub.sku sk 
on fdi.sku_num = sk.sku_num
inner join
(select hp.edw_hshld_num edw_hshld_num, hp.first_dt first_dt, H.chnl_cd chnl_cd from
		(
		select edw_hshld_num, min(ord_fr_act_dt) as first_dt
    	from lehub.HSHLD_PURCH_SUM H
    	group by 1
		)hp
		inner join lehub.HSHLD_PURCH_SUM H 
			on hp.edw_hshld_num = H.edw_hshld_num
			and hp.first_dt = H.ord_fr_act_dt
		inner join lehub.FSCL_CAL_DT fcd
			on hp.first_dt = fcd.CAL_DT	
		where fcd.FSCL_CAL_NUM = 4 
		and H.chnl_cd = 1
		and fcd.fscl_yr = 2023
		and fcd.cal_dt between '{min_date_23_shifted}' AND '{max_date_23_shifted}'
		
)HPS
on HPS.edw_hshld_num = VC.edw_hshld_num and HPS.first_dt = fdi.src_ord_dt
inner join lehub.FSCL_CAL_DT fcd
	on fdi.SRC_ORD_DT = fcd.CAL_DT
where fdi.REG_DMD_QTY > 0 
and fdi.BUS_UNIT_NUM = 1
and fcd.FSCL_CAL_NUM = 4 
and fcd.fscl_yr = 2023
and fdi.src_ord_dt between '{min_date_23_shifted}' AND '{max_date_23_shifted}'
and fdi.alt_bus_unit_num in (1,2)
group by 1
)
"""

UAT_QUERY_17 = f"""
with reactivated as (select
    vc.edw_hshld_num as hshl,
    min(fdi.src_ord_dt) as purchase_in_2023 
  from
    lehub.vw_consumer as vc
inner join lehub.FCT_DMD_ITEM as fdi
      on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM and fdi.src_ord_dt  between '{min_date_24}' and '{max_date_24}'
 join lehub.fscl_cal_dt                as fcd
	on fdi.src_ord_dt  = fcd.cal_dt   
  where fdi.bus_unit_num = 1
    and fdi.alt_bus_unit_num IN (1, 2)
    and fdi.reg_dmd_qty > 0
    and fdi.dmd_amt > 0
   and fcd.fscl_cal_num   = 4
   and fcd.fscl_yr = 2024
  group by 
    vc.edw_hshld_num 
    ) ,

 recency as (
select reactivated.hshl hshld , max(fdi.src_ord_dt) as lp_before_q1 , reactivated.purchase_in_2023, datediff(months , lp_before_q1 , '{min_date_24}') as months_between,
    case when months_between >60 then 'reactivated'
	 else '0' end as recency 
 from reactivated 
 join lehub.vw_consumer as vc
 on reactivated.hshl = vc.edw_hshld_num 
 left join (select fdi.CNSMR_NUM as cnsmr_num , fdi.src_ord_dt as src_ord_dt , fdi.sku_num as sku_num  from  lehub.FCT_DMD_ITEM fdi
 inner join lehub.sku as sk
    on fdi.sku_num = sk.sku_num 
where fdi.bus_unit_num = 1
    and fdi.alt_bus_unit_num IN (1, 2)
    and fdi.reg_dmd_qty > 0
    and fdi.dmd_amt > 0) fdi
      on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM and fdi.src_ord_dt < reactivated.purchase_in_2023
     group by 1 , 3 
)  


select count(distinct hshl) as reactivated_count_fscl_wk  from (
select * from 
reactivated join recency on reactivated.hshl = recency.hshld 
where recency = 'reactivated'
)
"""

UAT_QUERY_18 = f"""
with reactivated as (select
    vc.edw_hshld_num as hshl,
    min(fdi.src_ord_dt) as purchase_in_2023 
  from
    lehub.vw_consumer as vc
inner join lehub.FCT_DMD_ITEM as fdi
      on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM and fdi.src_ord_dt  between '{min_date_23}' and '{max_date_23}'
 join lehub.fscl_cal_dt                as fcd
	on fdi.src_ord_dt  = fcd.cal_dt   
  where fdi.bus_unit_num = 1
    and fdi.alt_bus_unit_num IN (1, 2)
    and fdi.reg_dmd_qty > 0
    and fdi.dmd_amt > 0
   and fcd.fscl_cal_num   = 4
   and fcd.fscl_yr = 2023
  group by 
    vc.edw_hshld_num 
    ) ,

 recency as (
select reactivated.hshl hshld , max(fdi.src_ord_dt) as lp_before_q1 , reactivated.purchase_in_2023, datediff(months , lp_before_q1 , '{min_date_23}') as months_between,
    case when months_between >60 then 'reactivated'
	 else '0' end as recency 
 from reactivated 
 join lehub.vw_consumer as vc
 on reactivated.hshl = vc.edw_hshld_num 
 left join (select fdi.CNSMR_NUM as cnsmr_num , fdi.src_ord_dt as src_ord_dt , fdi.sku_num as sku_num  from  lehub.FCT_DMD_ITEM fdi
 inner join lehub.sku as sk
    on fdi.sku_num = sk.sku_num 
where fdi.bus_unit_num = 1
    and fdi.alt_bus_unit_num IN (1, 2)
    and fdi.reg_dmd_qty > 0
    and fdi.dmd_amt > 0) fdi
      on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM and fdi.src_ord_dt < reactivated.purchase_in_2023
     group by 1 , 3 
)  


select count(distinct hshl) as reactivated_count_fscl_wk  from (
select * from 
reactivated join recency on reactivated.hshl = recency.hshld 
where recency = 'reactivated'
)
"""

UAT_QUERY_19 = f"""
with reactivated as (select
    vc.edw_hshld_num as hshl,
    min(fdi.src_ord_dt) as purchase_in_2023 
  from
    lehub.vw_consumer as vc
inner join lehub.FCT_DMD_ITEM as fdi
      on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM and fdi.src_ord_dt  between '{min_date_24_shifted}' AND '{max_date_24_shifted}'
 join lehub.fscl_cal_dt                as fcd
	on fdi.src_ord_dt  = fcd.cal_dt   
  where fdi.bus_unit_num = 1
    and fdi.alt_bus_unit_num IN (1, 2)
    and fdi.reg_dmd_qty > 0
    and fdi.dmd_amt > 0
   and fcd.fscl_cal_num   = 4
   and fcd.fscl_yr = 2024
  group by 
    vc.edw_hshld_num 
    ) ,

 recency as (
select reactivated.hshl hshld , max(fdi.src_ord_dt) as lp_before_q1 , reactivated.purchase_in_2023, datediff(months , lp_before_q1 , '{min_date_24_shifted}') as months_between,
    case when months_between >60 then 'reactivated'
	 else '0' end as recency 
 from reactivated 
 join lehub.vw_consumer as vc
 on reactivated.hshl = vc.edw_hshld_num 
 left join (select fdi.CNSMR_NUM as cnsmr_num , fdi.src_ord_dt as src_ord_dt , fdi.sku_num as sku_num  from  lehub.FCT_DMD_ITEM fdi
 inner join lehub.sku as sk
    on fdi.sku_num = sk.sku_num 
where fdi.bus_unit_num = 1
    and fdi.alt_bus_unit_num IN (1, 2)
    and fdi.reg_dmd_qty > 0
    and fdi.dmd_amt > 0) fdi
      on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM and fdi.src_ord_dt < reactivated.purchase_in_2023
     group by 1 , 3 
)  


select count(distinct hshl) as reactivated_count_fscl_wk  from (
select * from 
reactivated join recency on reactivated.hshl = recency.hshld 
where recency = 'reactivated'
)
"""


UAT_QUERY_20 = f"""
with reactivated as (select
    vc.edw_hshld_num as hshl,
    min(fdi.src_ord_dt) as purchase_in_2023 
  from
    lehub.vw_consumer as vc
inner join lehub.FCT_DMD_ITEM as fdi
      on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM and fdi.src_ord_dt  between '{min_date_23_shifted}' AND '{max_date_23_shifted}'
 join lehub.fscl_cal_dt                as fcd
	on fdi.src_ord_dt  = fcd.cal_dt   
  where fdi.bus_unit_num = 1
    and fdi.alt_bus_unit_num IN (1, 2)
    and fdi.reg_dmd_qty > 0
    and fdi.dmd_amt > 0
   and fcd.fscl_cal_num   = 4
   and fcd.fscl_yr = 2023
  group by 
    vc.edw_hshld_num 
    ) ,

 recency as (
select reactivated.hshl hshld , max(fdi.src_ord_dt) as lp_before_q1 , reactivated.purchase_in_2023, datediff(months , lp_before_q1 , '{min_date_23_shifted}') as months_between,
    case when months_between >60 then 'reactivated'
	 else '0' end as recency 
 from reactivated 
 join lehub.vw_consumer as vc
 on reactivated.hshl = vc.edw_hshld_num 
 left join (select fdi.CNSMR_NUM as cnsmr_num , fdi.src_ord_dt as src_ord_dt , fdi.sku_num as sku_num  from  lehub.FCT_DMD_ITEM fdi
 inner join lehub.sku as sk
    on fdi.sku_num = sk.sku_num 
where fdi.bus_unit_num = 1
    and fdi.alt_bus_unit_num IN (1, 2)
    and fdi.reg_dmd_qty > 0
    and fdi.dmd_amt > 0) fdi
      on vc.CUR_CNSMR_NUM = fdi.CNSMR_NUM and fdi.src_ord_dt < reactivated.purchase_in_2023
     group by 1 , 3 
)  


select count(distinct hshl) as reactivated_count_fscl_wk  from (
select * from 
reactivated join recency on reactivated.hshl = recency.hshld 
where recency = 'reactivated'
)
"""



print("SQL QUERIES UPDATED ")







