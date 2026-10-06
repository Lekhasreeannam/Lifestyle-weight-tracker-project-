import streamlit as st
import pandas as pd
import joblib

# Load model, scaler, and feature names
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

st.set_page_config(page_title="Lifestyle Weight Prediction", page_icon="⚖️")

st.title("Lifestyle Weight Prediction")
st.write("Enter the details below to predict weight.")

# User Inputs
stress = st.number_input("Stress Level")
calories = st.number_input("Calories Consumed")
protein = st.number_input("Protein (g)")
carbs = st.number_input("Carbs (g)")
fat = st.number_input("Fat (g)")

if st.button("Predict Weight"):

    input_df = pd.DataFrame([[stress, calories, protein, carbs, fat]],
                            columns=features)

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)

    st.success(f"Predicted Weight: {prediction[0]:.2f} kg")