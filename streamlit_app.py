import streamlit as st
import joblib
import numpy as np

# Title and description
st.set_page_config(page_title="E-Commerce Linear Regression", layout="centered")
st.title("📊 E-Commerce Purchase Predictor")
st.markdown("Predict the yearly spending of a customer based on their online activity.")

# Load the trained model
model = joblib.load("lm.pkl")

# User inputs for all 4 features
st.subheader("Enter Customer Info:")
avg_session_length = st.number_input("🕒 Avg. Session Length", min_value=0.0, format="%.2f")
time_on_app = st.number_input("📱 Time on App (minutes)", min_value=0.0, format="%.2f")
time_on_website = st.number_input("🌐 Time on Website (minutes)", min_value=0.0, format="%.2f")
membership_length = st.number_input("📅 Length of Membership (years)", min_value=0.0, format="%.2f")

# Predict button
if st.button("Predict Yearly Spending 💰"):
    # Make prediction
    input_data = np.array([[avg_session_length, time_on_app, time_on_website, membership_length]])
    prediction = model.predict(input_data)
    
    st.success(f"🤑 Predicted Yearly Amount Spent: **${prediction[0]:,.2f}**")
