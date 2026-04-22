import streamlit as st
import requests

st.set_page_config(page_title="Anomaly Detection", layout="centered")

st.title("🔥 Anomaly Detection System")

st.write("Enter temperature values to check anomaly:")

# Inputs
center_temp = st.number_input("Center Temperature", value=0.0)
max_temp = st.number_input("Max Temperature", value=0.0)
min_temp = st.number_input("Min Temperature", value=0.0)

# Button
if st.button("Predict"):
    data = {
        "center_temp": center_temp,
        "max_temp": max_temp,
        "min_temp": min_temp
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        result = response.json()

        st.subheader("Result")

        st.write(f"Reconstruction Error: {result['reconstruction_error']}")

        if result["anomaly"]:
            st.error("⚠️ Anomaly Detected!")
        else:
            st.success("✅ Normal Data")

    except:
        st.error("❌ API not running. Please start FastAPI first.")