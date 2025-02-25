import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(page_title="Auto Parts & Motorbike Selling", layout="wide")

# Title
st.title("🚀 Auto Parts & Motorbike Selling - Growth Mindset Dashboard")

# Sidebar Filters
category = st.sidebar.selectbox("Select Category", ["All", "Motorbikes", "Auto Parts"])
price_range = st.sidebar.slider("Select Price Range", 1000, 500000, (10000, 100000))

# ✅ Fixed Sample Data (All lists have same length)
data = pd.DataFrame({
    "Product": ["Yamaha R15", "Honda CG125", "Suzuki GS150", "Helmet", "Brake Pads", "Brake Shoo", "Battery", "Lights"],
    "Category": ["Motorbikes", "Motorbikes", "Motorbikes", "Auto Parts", "Auto Parts", "Auto Parts", "Auto Parts", "Auto Parts"],
    "Price": [400000, 250000, 350000, 5000, 2000, 500, 3000, 4500],
    "Sales": [120, 180, 90, 300, 450, 500, 678, 1000]
})

# Filter Data
if category != "All":
    data = data[data["Category"] == category]
data = data[(data["Price"] >= price_range[0]) & (data["Price"] <= price_range[1])]

# Display Data
st.write("### Available Products")
st.dataframe(data)

# Sales Chart
fig = px.bar(data, x="Product", y="Sales", color="Category", title="Sales Performance")
st.plotly_chart(fig)

# Feedback Form
st.write("### Customer Feedback")
name = st.text_input("Your Name")
feedback = st.text_area("Your Feedback")
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")
