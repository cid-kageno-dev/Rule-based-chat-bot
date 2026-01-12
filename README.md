##🤖 Simple Rule-Based Chatbot

#A beginner-friendly keyword-based chatbot written in Python.
This project uses deterministic, rule-based logic only—no AI, no machine learning, no external APIs.

Ideal for understanding how classic chatbots worked before the hype train arrived.


---

✨ Features

Keyword-based input matching

Randomized replies for natural variation

Clean, modular project structure

Terminal (CLI) support

Optional Flask API for backend usage

Easy to extend with new rules



---

⚙️ How It Works

1. User input is normalized (lowercase, punctuation removed)


2. Input is matched against predefined keywords


3. A random response is selected from the matched rule


4. If nothing matches, a fallback response is returned



Simple logic. Predictable behavior. No magic.


---

🧩 Requirements

Python 3.8+

No external dependencies for CLI mode

Flask (only required for API mode)


Install Flask (API mode only):

pip install flask


---

▶️ Running the Chatbot (CLI)

python cli.py

Example:

You: hello
ChatBot: Hello.

Type bye or quit to exit.


---

🌐 Flask API (Backend Mode)

Run the chatbot as a lightweight HTTP API.

Start the Server

python app.py

Server runs at:

http://localhost:5000


---

🔌 API Endpoint

POST /chat

Request (JSON):

{
  "message": "hello"
}

Response (JSON):

{
  "author": "Cid Kageno",
  "reply": "Greetings. Coincidentally."
}


---

🩺 Root Health Check

GET /

Response:

Chatbot backend running | Author: Cid Kageno

Useful for deployment health checks (Render, Railway, etc.).


---

🚀 Deployment Notes

Reads the PORT environment variable

Compatible with Render, Railway, and Heroku

No database or external services required



---

🎯 Use Cases

Learning Python fundamentals

Understanding rule-based systems

Practicing Flask APIs

Lightweight chatbot experiments

Educational demos



---

👤 Author

Cid Kageno

Minimal logic. Deterministic behavior. Built to be understood.
<img src="https://user-images.githubusercontent.com/74038190/212284136-03988914-d899-44b4-b1d9-4eeccf656e44.gif" width="500">
<br><br>
