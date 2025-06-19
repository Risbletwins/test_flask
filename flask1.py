from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route('/api', methods=['GET'])
def handle_get():
    data = request.args.get('data', 'No data')
    print(f"Received from ESP32: {data}")
    return f"Got: {data}", 200
@app.route("/getdata", methods=["GET"])
def get_data():
    return "Here is your data!"

app.run(host='0.0.0.0', port=5000)
