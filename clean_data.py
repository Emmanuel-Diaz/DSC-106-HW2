import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

%matplotlib inline


daily_sales = pd.read_csv('daily_sales.csv')
monthly_sales = pd.read_csv('monthly_sales.csv')

daily_sales['Tot_CF'] = daily_sales.apply(lambda row: row['CF-NE'] + row['CF-SW'] + row['CF-SE'] + row['CF-C'] + row['CF-NW'], axis=1)
daily_sales['Tot_FF'] = daily_sales.apply(lambda row: row['FF-NE'] + row['FF-SW'] + row['FF-SE'] + row['FF-C'] + row['FF-NW'], axis=1)
daily_sales['Tot_HM'] = daily_sales.apply(lambda row: row['HM-NE'] + row['HM-SW'] + row['HM-SE'] + row['HM-C'] + row['HM-NW'], axis=1)

monthly_sales['Tot_CF'] = monthly_sales.apply(lambda row: row['CF-NE'] + row['CF-SW'] + row['CF-SE'] + row['CF-C'] + row['CF-NW'], axis=1)
monthly_sales['Tot_FF'] = monthly_sales.apply(lambda row: row['FF-NE'] + row['FF-SW'] + row['FF-SE'] + row['FF-C'] + row['FF-NW'], axis=1)
monthly_sales['Tot_HM'] = monthly_sales.apply(lambda row: row['HM-NE'] + row['HM-SW'] + row['HM-SE'] + row['HM-C'] + row['HM-NW'], axis=1)

daily_sales = daily_sales.rename(columns={'Unnamed: 0': 'DayOTW'})
daily_sales.to_csv('daily_sales_cleaned.csv')
monthly_sales.to_csv('monthly_sales_cleaned.csv')
