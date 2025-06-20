from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the current message to send to ESP32
current_data = {"message": "Hello ESP32!"}

@app.route("/")
def home():
    return "ESP32 Communication Server is Running"

# Endpoint ESP32 will call to get the message
@app.route("/get-data", methods=["GET"])
def get_data():
    return jsonify(current_data)

# # You can update the message using this endpoint
# @app.route("/set-data", methods=["POST"])
# def set_data():
#     data = request.json
#     if "message" in data:
#         current_data["message"] = data["message"]
#         return jsonify({"status": "success", "new_message": current_data["message"]})
#     return jsonify({"status": "error", "reason": "No message found"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Make sure it's accessible on your network
