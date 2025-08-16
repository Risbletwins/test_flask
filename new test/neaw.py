import requests

url = "http://localhost:5000/api"  # Replace with your endpoint
data = {
    "name": "Nuslan",
    "age": 17
}

response = requests.post(url, json=data)  # Sends JSON data
print("Status:", response.status_code)
print("Response:", response.text)
