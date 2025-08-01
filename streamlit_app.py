import streamlit as st
import pandas as pd
import numpy as np
import joblib


# Load model
model = joblib.load("lm.pkl")

st.title("🛒 E-Shop Spend Predictor")
st.write("Predict how much a customer will spend yearly based on their behavior.")

# Input features
avg_session_length = st.number_input("Average Session Length", 0.0, 40.0, 32.0)
time_on_app = st.number_input("Time on App", 0.0, 40.0, 12.0)
time_on_website = st.number_input("Time on Website", 0.0, 40.0, 38.0)
length_of_membership = st.number_input("Length of Membership (in years)", 0.0, 10.0, 4.0)

# Make prediction
input_data = pd.DataFrame([[avg_session_length, time_on_app, time_on_website, length_of_membership]],
                          columns=["Avg. Session Length", "Time on App", "Time on Website", "Length of Membership"])

if st.button("Predict Spending"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Yearly Spending: ${prediction:.2f}")

