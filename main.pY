
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "THORAPPAN KOCHUNNI 2.0",
        "status": "Running",
        "message": "Personal AI Assistant"
    })

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    message = data.get("message", "")

    return jsonify({
        "user_message": message,
        "reply": "Welcome to THORAPPAN KOCHUNNI AI!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
