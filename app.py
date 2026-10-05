"""
SentinelAI CI Demo Application
Experiment 3: CI Pipeline using GitHub Actions and Jenkins
"""
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to SentinelAI CI Demo",
        "status": "running",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat()
    })


@app.route('/health')
def health():
    return jsonify({"status": "healthy", "timestamp": datetime.utcnow().isoformat()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
