import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

st.title('E-commerce-public-dataset')

# Tulisan dengan wrapping
st.write('BUSINESS QUESTIONS WITH DATA ANALYSIS')
st.write('1. Is there a trend in monthly sales growth over time, and are there certain months that show significant increases or decreases?')
st.write('2. What is the distribution of payment methods in e-commerce transactions, and are there payment methods that are more dominant than others?')
st.write('3. What is the distribution of customer reviews based on product review scores in e-commerce platforms, and are there patterns or trends that can be identified from this distribution?')
st.write('4. How do sellers perform on e-commerce platforms based on the number of products sold, and who are the top 10 sellers based on the number of products sold?')
st.write('5. What is the distribution of customer locations by state?')


st.write('ANSWER')
# ======================================================================
# Pertanyaan 1
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
order_dataset = pd.read_csv("orders_dataset.csv")
order_items_dataset = pd.read_csv("order_items_dataset.csv")

# Merge datasets
merged_data = pd.merge(order_dataset, order_items_dataset, on="order_id")

# Convert 'order_purchase_timestamp' to datetime
merged_data['order_purchase_timestamp'] = pd.to_datetime(merged_data['order_purchase_timestamp'])

# Extract month from 'order_purchase_timestamp'
merged_data['order_month'] = merged_data['order_purchase_timestamp'].dt.to_period('M')

# Group by month and sum the total sales
monthly_sales = merged_data.groupby('order_month')['price'].sum()

# Streamlit code
st.title('Trend Penjualan Bulanan')
st.write("Total Penjualan per Bulan")
st.line_chart(monthly_sales)

st.write('Analysis: To see monthly sales trends, I use orders_dataset and order_items_dataset. to see in what month the highest sales occurred. And there is sales growth, this can be seen from the output above. sales always experience a positive increase, although there was some decline in December 2018. However, this was not too significant and did not decrease from initial sales in November 2017. The highest sales occurred in October to November 2018. A significant decline in sales occurred in December 2018 touched total sales of 0.7 from the previous November 2018 touched total sales of 1.0')

# ===============================================================================
# Pertanyaan 2
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
order_payments = pd.read_csv("order_payments_dataset.csv")

# Calculate payment method distribution
payment_method_distribution = order_payments['payment_type'].value_counts()

# Streamlit code
st.title('Distribusi Metode Pembayaran')
st.bar_chart(payment_method_distribution)

st.write('Based on the data above, the highest use of payment methods is using credit cards with the number of transactions reaching almost 80,000. Followed by boleto with a number of transactions of 20,000, then vouchers with almost 5,000 transactions and debit cards which are the least used in payment methods.')

# ================================================================================
# Pertanyaan 4
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
order_reviews = pd.read_csv("order_reviews_dataset.csv")

# Calculate customer satisfaction distribution
customer_satisfaction = order_reviews['review_score'].value_counts().sort_index()

# Streamlit code
st.title('Distribusi Ulasan Pelanggan Berdasarkan Skor Ulasan Produk')
st.bar_chart(customer_satisfaction)

st.write('Analysis: Based on the data above, it can be seen that customers who gave the highest review score of 5 received the highest number of reviews, namely almost 60,000 reviews. In second place is a review score of 4 with a total of 19,000 reviews. number 3 has a review score of 1 and has a total of 12,000 reviews. and the fewest reviews were under 10,000 reviews with a review score of 2. The pattern that can be seen from this analysis is that most buyers were satisfied with the goods and services received, seen from 57,000 reviews giving a review score of 5.')

# ================================================================================
# Pertanyaan 5
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
order_items = pd.read_csv("order_items_dataset.csv")
sellers = pd.read_csv("sellers_dataset.csv")

# Merge datasets based on seller_id
merged_data = pd.merge(order_items, sellers, on="seller_id")

# Calculate total products sold per seller
products_sold_per_seller = merged_data.groupby('seller_id')['product_id'].count().sort_values(ascending=False)

# Streamlit code
st.title('Top 10 Penjual Berdasarkan Jumlah Produk Terjual')
st.bar_chart(products_sold_per_seller.head(10))

st.write('Analysis: Judging from the data above, the sales performance made by traders is very visible in the direction of positive margins. This can be seen from the number of products sold reaching 2000 units. It shows high interest and purchasing power by buyers, this can make it a good target market. To see this, I created 10 sellers with the highest number of products sold.')

# ==============================================================================
# Pertanyaan 7
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
customers = pd.read_csv("customers_dataset.csv")

# Streamlit code
st.title('Distribusi Lokasi Pelanggan')
st.bar_chart(customers['customer_state'].value_counts())
st.bar_chart(customers)

st.write('Analysis: By looking at the data above, it can be seen that the largest number of buyers are in SP locations with a number of customers reaching 45,000 and the fewest are in AM with a number of customers below 5,000. This can be a prediction for the future market regarding buyer interest. Because if there are many residents or buyers in an area, then the sale of goods and distribution will occur more quickly.')
