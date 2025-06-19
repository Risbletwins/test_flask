from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def handle_get():
    # Get query parameter 'data'
    data = request.args.get('data', 'No data received')
    
    # Print to terminal (optional)
    print(f"Received data: {data}")
    
    # Send response back to ESP32
    return f"Received: {data}", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
