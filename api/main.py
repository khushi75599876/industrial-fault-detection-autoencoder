from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from tensorflow.keras.models import load_model

# Initialize app
app = FastAPI()

# Load model
model = load_model("models/autoencoder_model.keras")

# Set threshold (you can tune this later)
THRESHOLD = 0.03


# ✅ Input schema (VERY IMPORTANT for Swagger)
class InputData(BaseModel):
    center_temp: float
    max_temp: float
    min_temp: float


# Home route
@app.get("/")
def home():
    return {"message": "Anomaly Detection API is running"}


# Prediction route
@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert input to numpy array
        input_data = np.array([
            data.center_temp,
            data.max_temp,
            data.min_temp
        ]).reshape(1, -1)

        # Model prediction (reconstruction)
        reconstructed = model.predict(input_data)

        # Calculate reconstruction error
        error = np.mean((input_data - reconstructed) ** 2)

        # Determine anomaly
        anomaly = error > THRESHOLD

        return {
            "reconstruction_error": float(error),
            "anomaly": bool(anomaly)
        }

    except Exception as e:
        return {"error": str(e)}