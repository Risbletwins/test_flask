from flask import Flask, request  # Flask's request for handling incoming requests
import requests  # The requests library for sending HTTP requests

app = Flask(__name__)

# ESP32 IP address and endpoint
ESP32_URL = "http://192.168.10.160/api"  # Replace with your ESP32's IP address

@app.route('/send-data', methods=['POST'])
def send_to_esp32():
    try:
        # Get JSON data from the incoming POST request
        data = request.get_json()
        if not data:
            return {"error": "No JSON data provided"}, 400

        # Send POST request to ESP32 using requests (not request)
        response = requests.post(ESP32_URL, json=data, timeout=5)
        
        # Check response from ESP32
        if response.status_code == 200:
            return {"message": "POST request sent to ESP32 successfully", "esp32_response": response.json()}, 200
        else:
            return {"error": f"ESP32 request failed with status code {response.status_code}"}, response.status_code
    except requests.exceptions.RequestException as e:  # Use requests.exceptions
        return {"error": f"Request to ESP32 failed: {str(e)}"}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)