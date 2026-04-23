# 🔥 Industrial Fault Detection using Autoencoder

## 🚀 Overview

This project is an end-to-end anomaly detection system built using an Autoencoder neural network. It detects abnormal patterns in industrial sensor data based on reconstruction error.

---

## 🧠 How it Works

* Autoencoder is trained on **normal data**
* During prediction:

  * Input is reconstructed
  * Reconstruction error is calculated
* If error > threshold → **Anomaly**
* Else → **Normal**

---

## 🛠️ Tech Stack

* Python
* TensorFlow / Keras
* FastAPI (for backend API)
* Streamlit (for frontend UI)
* NumPy, Pandas

---

## ⚙️ Project Structure

```
api/        → FastAPI backend
app/        → Streamlit frontend
models/     → Trained autoencoder model
data/       → Dataset
```

---

## ▶️ How to Run (Local)

### 1. Start FastAPI

```
python -m uvicorn api.main:app --reload
```

### 2. Start Streamlit

```
streamlit run app/app.py
```

---

## 📊 Features

* Real-time anomaly detection
* Interactive UI
* REST API for model inference
* Reconstruction error visualization

---

## 📌 Future Improvements

* Deploy on cloud (AWS / GCP)
* Add real-time IoT data integration
* Improve threshold tuning

---

## 👩‍💻 Author

Khushi Patel
