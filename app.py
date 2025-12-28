from flask import Flask, request, jsonify
from chatbot.engine import get_response
import os

app = Flask(__name__)

# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    reply = get_response(message)
    return jsonify({"reply": reply})

# Root route for testing
@app.route("/")
def root():
    return "Chatbot backend running"

# Entry point for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render assigns PORT
    app.run(host="0.0.0.0", port=port)
