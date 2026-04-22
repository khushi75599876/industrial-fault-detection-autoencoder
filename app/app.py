import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

st.set_page_config(page_title="Anomaly Detection", layout="centered")

st.title("🔥 Industrial Fault Detection System")

st.write("Enter temperature values to check anomaly:")

# Load model
model = load_model("models/autoencoder_model.keras")

THRESHOLD = 0.01

# Inputs
center_temp = st.number_input("Center Temperature", value=0.0)
max_temp = st.number_input("Max Temperature", value=0.0)
min_temp = st.number_input("Min Temperature", value=0.0)

# Button
if st.button("Predict"):
    input_data = np.array([[center_temp, max_temp, min_temp]])

    reconstructed = model.predict(input_data)
    error = np.mean((input_data - reconstructed) ** 2)

    st.subheader("Result")
    st.write(f"Reconstruction Error: {error}")

    if error > THRESHOLD:
        st.error("⚠️ Anomaly Detected!")
    else:
        st.success("✅ Normal Data")