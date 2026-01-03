"""Mobile Price Classification App using Streamlit (5 Features)"""

import streamlit as st
import joblib
import numpy as np

# ======================
# Load model and scaler
# ======================
model = joblib.load("logistic_model_5f.pkl")
scaler = joblib.load("scaler_5f.pkl")

# ======================
# Page config
# ======================
st.set_page_config(
    page_title="Mobile Price Classification",
    page_icon="📱",
    layout="centered"
)

st.title("📱 Mobile Price Classification App")
st.markdown(
    "Predict the **price range** of a mobile phone using **5 key features**."
)

st.divider()

# ======================
# User Inputs
# ======================
st.subheader("🔧 Enter Mobile Specifications")

battery = st.number_input(
    "🔋 Battery Power (mAh)",
    min_value=500,
    max_value=5000,
    step=100
)

ram = st.number_input(
    "💾 RAM (MB)",
    min_value=256,
    max_value=8000,
    step=256
)

px_width = st.number_input(
    "🖥️ Pixel Width",
    min_value=0,
    max_value=2000
)

px_height = st.number_input(
    "🖥️ Pixel Height",
    min_value=0,
    max_value=2000
)

mobile_wt = st.number_input(
    "⚖️ Mobile Weight (grams)",
    min_value=80,
    max_value=300
)

st.divider()

# ======================
# Prediction
# ======================
if st.button("🔍 Predict Price Range"):
    input_data = np.array([[
        battery,
        ram,
        px_width,
        px_height,
        mobile_wt
    ]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    labels = {
        0: "Low Cost 📉",
        1: "Medium Cost 📊",
        2: "High Cost 📈",
        3: "Very High Cost 🚀"
    }

    st.success(f"### Predicted Price Range: **{labels[prediction]}**")
