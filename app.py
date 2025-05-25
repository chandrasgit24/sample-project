from flask import Flask, render_template
import os
from azure.ai.anomalydetector import AnomalyDetectorClient
from azure.core.credentials import AzureKeyCredential

app = Flask(__name__)

# Initialize Anomaly Detector client (replace placeholders)
ANOMALY_DETECTOR_ENDPOINT = os.getenv("https://anomaly-detector-traffic.services.ai.azure.com/")
ANOMALY_DETECTOR_KEY = os.getenv("E8toUSEWD1zlnTH2rfD3HTWiGT2VoKeAOgra29Nb8l0Qcd45N5I7JQQJ99BEACBsN54XJ3w3AAAAACOGlYR7")

# Only initialize client if keys are provided (avoids errors if keys are missing)
try:
    client = AnomalyDetectorClient(
        endpoint=ANOMALY_DETECTOR_ENDPOINT,
        credential=AzureKeyCredential(ANOMALY_DETECTOR_KEY)
    )
except Exception as e:
    print(f"⚠️ Anomaly Detector initialization failed: {e}")
    client = None

@app.route('/')
def home():
    print("Trying to render index.html from:", os.listdir("templates"))
    return render_template('index.html')

@app.route('/predict-traffic')
def predict_traffic():
    if not client:
        return "Anomaly Detector not configured. Check server logs.", 500
    
    # Mock traffic data (replace with real data from logs/database)
    traffic_data = [10, 12, 11, 15, 20, 50, 60, 55, 50, 12, 11, 10]  # Example spike at 50-60
    
    try:
        request = {
            "series": [{"value": value} for value in traffic_data],
            "granularity": "hourly"
        }
        response = client.detect_last_point(request)
        return {
            "is_anomaly": response.is_anomaly,
            "message": "⚠️ Traffic anomaly detected!" if response.is_anomaly else "Traffic normal."
        }
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run()
