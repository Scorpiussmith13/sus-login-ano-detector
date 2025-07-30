from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
from tensorflow.keras.models import load_model

app = FastAPI()

# Load resources once at startup
iso_forest = joblib.load("models/isolation_forest_model.joblib")
autoencoder = load_model("models/autoencoder_model.keras")
scaler = joblib.load("scaler.joblib")

# Define the expected input
class LoginFeatures(BaseModel):
    hour: int
    day_of_week: int
    device_type_enc: int
    browser_enc: int
    geo_location_enc: int
    user_id_enc: int
    session_duration: float
    time_since_last_login: float
    failed_logins_before_success: int
    unique_sessions_today: int

@app.post("/predict")
def predict(input: LoginFeatures):
    features = np.array([list(input.dict().values())])
    features_scaled = scaler.transform(features)

    # Isolation Forest anomaly score
    iso_score = iso_forest.decision_function(features_scaled)[0]  # higher = more normal

    # Autoencoder reconstruction error
    ae_recon = autoencoder.predict(features_scaled)
    ae_error = np.mean(np.square(features_scaled - ae_recon), axis=1)[0]

    # Normalize both scores for fuse (use fixed range for single input)
    # For demo: numbers are for display only; in production, use scaler from train set or fit on server startup for batch
    iso_norm = (iso_score + 0.5) / 1.0  # Simple min-max if typical IF scores [-0.5,0.5]
    ae_norm = 1.0 / (1.0 + ae_error)    # Inverse error for normalization

    combined_score = (iso_norm + ae_norm) / 2

    # Threshold from experimentation (adjust as you wish)
    threshold = 0.5
    is_anomaly = combined_score < threshold

    return {
        "is_anomaly": bool(is_anomaly),
        "iso_score": float(iso_score),
        "ae_error": float(ae_error),
        "combined_score": float(combined_score)
    }
