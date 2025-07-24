#simulation of a device for testing purposes

from flask import Flask, jsonify, request
# This file contains a mock device that simulates a real device for testing purposes..py
app = Flask(__name__)
# This file contains tests for the mock device.

valid_users = {
    "admin": "admin123",
    "guest": "123456"
}

@app.route('/login', methods=['POST'])

def login():
    username = request.form.get('username')
# This file contains tests for the mock device.
    password = request.form.get('password')
    if username == 'admin' and password == 'admin123':
        return "<h1>dashboard</h1>", 200
    return "Unauthorized", 401

@app.route("/api/status")
def status():
    return jsonify({
        "status": "ok",
        "projecting": True,
        "connected": True
        })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
    