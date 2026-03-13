import pandas as pd
import numpy as np


df = pd.read_csv('data\lumina_master_dataset.csv')

print(df.head())
print(df.info())


#
df = df.drop_duplicates()

date_columns = [
    'order_purchase_timestamp', 
    'order_delivered_customer_date', 
    'order_estimated_delivery_date'
]

for col in date_columns:
    df[col] = pd.to_datetime(df[col])



df['delivery_time_days'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days


df['delivery_delay_days'] = (df['order_delivered_customer_date'] - df['order_estimated_delivery_date']).dt.days

df['delivery_status'] = np.where(df['delivery_delay_days'] > 0, 'En retard', 'A l\'heure / En avance')

print(df[['order_id', 'delivery_time_days', 'delivery_delay_days', 'delivery_status']].head())


df.to_csv('lumina_powerbi_ready.csv', index=False)