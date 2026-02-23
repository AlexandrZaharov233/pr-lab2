from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/fetch-data", methods=["GET"])
def fetch_data():
    response = requests.get("http://lab2.1:5000/data")
    return response.json()

@app.route("/send-data", methods=["POST"])
def send_data():
    data = request.json
    response = requests.post("http://lab2.1:5000/data", json=data)
    return response.json()

@app.route("/update-data", methods=["PUT"])
def update_data():
    data = request.json
    response = requests.put("http://lab2.1:5000/data", json=data)
    return response.json()

@app.route("/delete-data", methods=["DELETE"])
def delete_data():
    key = request.args.get("key")
    response = requests.delete("http://lab2.1:5000/data?key={key}")
    return response.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
