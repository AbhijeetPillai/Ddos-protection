from flask import Flask, jsonify
import random
import time
from threading import Thread
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory log to store traffic data
traffic_logs = []

# Function to generate simulated traffic data
def generate_traffic_data():
    while True:
        current_requests = random.choice([50, 2000])  # Simulated traffic
        status = "normal" if current_requests <= 1000 else "DDoS detected"
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        traffic_logs.append({
            "requests_per_second": current_requests,
            "status": status,
            "timestamp": timestamp
        })
        time.sleep(2)  # Simulate time delay for each log

@app.route('/traffic')  # Ensure this route is defined
def traffic():
    return jsonify(traffic_logs[-5:])  # Return the last 5 logs

if __name__ == "__main__":
    # Start the traffic data generation in a separate thread
    traffic_thread = Thread(target=generate_traffic_data)
    traffic_thread.start()
    
    # Run Flask server on localhost:5500
    app.run(debug=True, port=5000)

