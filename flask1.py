from flask import Flask, request, jsonify

app = Flask(__name__)

current_data = "meaw to esp32"

@app.route("/")
def home():
    return "ESP32 Communication Server is Running"

@app.route("/get-data", methods=["GET","POST"])
def get_data():
    return current_data

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 
