import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.title('E-commerce-public-dataset')

# cara mengambil dataset dari github
dataset = pd.read_csv 


order_dataset = pd.read_csv("orders_dataset.csv")
order_items_dataset = pd.read_csv("order_items_dataset.csv")

merged_data = pd.merge(order_dataset, order_items_dataset, on="order_id")
merged_data['order_purchase_timestamp'] = pd.to_datetime(merged_data['order_purchase_timestamp'])
merged_data['order_month'] = merged_data['order_purchase_timestamp'].dt.to_period('M')

monthly_sales = merged_data.groupby('order_month')['price'].sum()

plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', marker='o', color='green')
plt.title('Trend Penjualan Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Total Penjualan')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()