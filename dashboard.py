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


st.write('ANSWER')
# ======================================================================
# Pertanyaan 1
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
order_dataset = pd.read_csv("orders_dataset.csv")
order_items_dataset = pd.read_csv("order_items_dataset.csv")

# Merge data
merged_data = pd.merge(order_dataset, order_items_dataset, on="order_id")
merged_data['order_purchase_timestamp'] = pd.to_datetime(merged_data['order_purchase_timestamp'])
merged_data['order_month'] = merged_data['order_purchase_timestamp'].dt.to_period('M')

# Calculate monthly sales
monthly_sales = merged_data.groupby('order_month')['price'].sum()

# Streamlit code
st.write("## Trend Penjualan Bulanan")
st.line_chart(monthly_sales)

# ===============================================================================
# Pertanyaan 2
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
order_payments = pd.read_csv("order_payments_dataset.csv")

# Calculate payment method distribution
payment_method_distribution = order_payments['payment_type'].value_counts()

# Streamlit code
st.write("## Distribusi Metode Pembayaran")
st.bar_chart(payment_method_distribution)

# ================================================================================
# Pertanyaan 3
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
order_reviews = pd.read_csv("order_reviews_dataset.csv")

# Calculate customer satisfaction distribution
customer_satisfaction = order_reviews['review_score'].value_counts().sort_index()

# Streamlit code
st.write("## Distribusi Ulasan Pelanggan Berdasarkan Skor Ulasan Produk")
st.bar_chart(customer_satisfaction)

# ================================================================================
# Pertanyaan 4
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
st.write("## Top 10 Penjual Berdasarkan Jumlah Produk Terjual")
st.bar_chart(products_sold_per_seller.head(10))


# =============================================================================

st.write('Conclusion question 1')
st.write('Based on the analysis carried out for question 1, several conclusions can be drawn. Monthly sales trends indicate a general upward trajectory, punctuated by occasional minor declines. Despite a decrease in sales in December 2018, figures never fell below the initial levels observed in November 2017. The peak of sales occurred during the period from October to November 2018, indicating the business achieved its highest sales performance during that time. Although there was a significant decline in sales in December 2018, dropping to 0.7 compared to the total sales in November 2018 which reached 1.0, sales remained relatively high compared to the beginning of the observation period. Thus, it can be concluded that despite fluctuations in monthly sales, the business experienced overall positive growth throughout the observed period, with the peak of sales occurring in October to November 2018.') 
st.write('Conclusion question 2')
st.write('Based on the analysis carried out for question 2, it is evident that credit cards are the most preferred payment method, with nearly 80,000 transactions recorded. Following credit cards, boleto is the second most utilized payment method, with approximately 20,000 transactions. Vouchers are the third most used payment method, with nearly 5,000 transactions, while debit cards have the lowest usage among the listed payment methods. Therefore, the conclusion drawn from this data is that credit cards are the most popular choice among customers for making payments, followed by boleto, vouchers, and debit cards in descending order of preference.')
st.write('Conclusion question 3')
st.write('Based on the analysis carried out for question 3, it is evident that the majority of customers are highly satisfied with the goods and services they received, as indicated by the distribution of review scores. The highest number of reviews, nearly 60,000, were given a score of 5, reflecting a high level of satisfaction among customers. Following closely behind, reviews with a score of 4 totaled approximately 19,000, indicating a significant level of satisfaction as well. Despite being the lowest score, reviews with a score of 1 still amounted to 12,000, suggesting that dissatisfaction among customers is relatively low. Additionally, there were fewer reviews with scores of 2, indicating a minor level of dissatisfaction. Overall, the pattern observed from this analysis is that the majority of buyers expressed satisfaction with the goods and services provided, particularly evident in the high number of reviews with a score of 5.')
st.write('Conclusion question 4') 
st.write('Based on the analysis carried out for question 4, it is evident that the sales performance of traders is highly positive, as indicated by the significant number of products sold, reaching up to 2000 units. This indicates a strong interest and purchasing power among buyers, highlighting a potentially lucrative target market. To further analyze this, the top 10 sellers with the highest number of products sold were identified. These sellers represent key players in the market with high sales volumes, reinforcing the notion of a thriving market with ample opportunities for growth and profitability. Therefore, based on the sales performance and the identified top sellers, it can be concluded that the market presents promising prospects for traders and businesses.')




