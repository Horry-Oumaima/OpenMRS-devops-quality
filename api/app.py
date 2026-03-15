from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Quality DevOps API",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/users")
def users():
    return jsonify({
        "users": [
            {"id": 1, "name": "oumaima"},
            {"id": 2, "name": "horry"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)