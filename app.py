# ACC102 Mini Assignment - Track4 Interactive Data Analysis Tool
# Student Name: [tianqi.lu] | Student ID: [2469622]
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Sales trend line chart
st.subheader("3. Monthly Sales Trend")
fig1, ax1 = plt.subplots(figsize=(10, 4))
for brand in sales_data.columns:
    ax1.plot(sales_data.index, sales_data[brand], label=brand, linewidth=2)
ax1.legend()
ax1.grid(alpha=0.3)
plt.tight_layout()
st.pyplot(fig1)

# Annual sales comparison bar chart
st.subheader("4. Annual Sales Comparison")
fig2, ax2 = plt.subplots(figsize=(8, 3))
total_sales.plot(kind="bar", ax=ax2, color=["#FF5733", "#33FF57", "#3357FF", "#FF33A6", "#F3FF33"])
ax2.grid(axis="y", alpha=0.3)
plt.tight_layout()
st.pyplot(fig2)

# Key business insights
st.success("5. Key Business Insights")
st.write("✅ Walmart achieves the highest total retail sales in 2025")
st.write("✅ All five retail brands show a stable growth trend")
st.write("✅ Aldi has the smallest sales base but strong growth momentum")