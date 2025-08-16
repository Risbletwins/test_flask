from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    # If sent as JSON
    json_data = request.get_json()
    print("JSON Data:", json_data)

    return {"status": "received"}, 200

if __name__ == '__main__':
    app.run(debug=True)
