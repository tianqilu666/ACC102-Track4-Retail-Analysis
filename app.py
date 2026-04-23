# ACC102 Mini Assignment - Track4 Interactive Data Analysis Tool
# Student Name: [tianqilu] | Student ID: [2469622]
import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="Retail Sales Analyzer", page_icon="🛒")
st.title("2025 Global Retail Sales Interactive Analysis")
st.markdown("### ACC102 Track4 | Business Data Product")

# Generate simulated retail sales data
months = pd.date_range(start="2025-01-01", periods=12, freq="M")
retail_brands = ["Walmart", "Carrefour", "Costco", "Tesco", "Aldi"]
np.random.seed(2026)

sales_data = pd.DataFrame(index=months)
for brand in retail_brands:
    base_value = [45, 28, 32, 25, 18][retail_brands.index(brand)]
    sales_data[brand] = base_value + np.linspace(0, 10, 12) + np.random.normal(0, 1.5, 12)

# Data preview section
st.subheader("1. Monthly Sales Data Preview")
st.dataframe(sales_data.round(2), use_container_width=True)

# Total annual sales calculation
st.subheader("2. Total Annual Sales (Billion USD)")
total_sales = sales_data.sum().sort_values(ascending=False)
st.dataframe(total_sales.round(2), use_container_width=True)

# Native Streamlit charts (no matplotlib needed)
st.subheader("3. Monthly Sales Trend")
st.line_chart(sales_data)

st.subheader("4. Annual Sales Comparison")
st.bar_chart(total_sales)

# Key business insights
st.success("5. Key Business Insights")
st.write("✅ Walmart achieves the highest total retail sales in 2025")
st.write("✅ All five retail brands show a stable growth trend")
st.write("✅ Aldi has the smallest sales base but strong growth momentum")
