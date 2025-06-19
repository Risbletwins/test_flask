from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def handle_get():
    data = request.args.get('data', 'No data')
    print(f"Received from ESP32: {data}")
    return f"Got: {data}", 200

app.run(host='0.0.0.0', port=5000)
