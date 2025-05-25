# Generated using ChatGPT
import requests
import json
from datetime import datetime, timedelta

endpoint = "https://anomaly-detector-traffic.services.ai.azure.com/"
api_key = "E8toUSEWD1zlnTH2rfD3HTWiGT2VoKeAOgra29Nb8l0Qcd45N5I7JQQJ99BEACBsN54XJ3w3AAAAACOGlYR7"

url = endpoint + "/anomalydetector/v1.1/timeseries/entire/detect"

# Generate dummy web traffic data (1 data point per hour)
data = {
    "series": [],
    "granularity": "hourly"
}

start_time = datetime.utcnow() - timedelta(hours=24)
for i in range(24):
    timestamp = start_time + timedelta(hours=i)
    value = 100 + (i % 6) * 10  # Simulate traffic
    if i == 20:
        value = 300  # Simulate spike
    data["series"].append({
        "timestamp": timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "value": value
    })

headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": api_key
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

# Output anomalies
for i, is_anomaly in enumerate(result["isAnomaly"]):
    if is_anomaly:
        print(f"Anomaly detected at {data['series'][i]['timestamp']} with value {data['series'][i]['value']}")
