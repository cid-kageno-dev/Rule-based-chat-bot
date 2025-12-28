- Animated Laptop Banner
<img src="https://github.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/assets/74038190/80728820-e06b-4f96-9c9e-9df46f0cc0a5" width="600">
<br><br>
---

Simple Rule-Based Chatbot 🤖

A beginner-friendly, keyword-based chatbot written in Python.
This project does not use AI or machine learning—it relies entirely on deterministic, rule-based logic.


---

Features

Keyword-based input matching

Randomized responses for natural variation

Clean, modular project structure

Works in the terminal (CLI)

Optional Flask API for backend usage

Easy to extend with new rules



---

How It Works

1. User input is normalized (lowercase, punctuation removed)


2. Input is checked against predefined keywords


3. A random response is selected from the matched category


4. If no keyword matches, a default fallback response is returned




---

Requirements

Python 3.8+

No external dependencies for CLI mode

Flask (only required for API mode)


Install Flask if using the API:

pip install flask


---

Running the Chatbot (CLI)

python cli.py

Example:

You: hello
ChatBot: …Hello.

Type bye or quit to exit.


---

Flask API (Backend Mode)

The chatbot can also run as a simple HTTP API using Flask.

Start the Server

python app.py

Server will run on:

http://localhost:5000


---

API Endpoint

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

Root Test Endpoint

GET /

Returns:

Chatbot backend running | Author: Cid Kageno

Useful for deployment health checks (Render, Railway, etc.).


---

Deployment Notes

The Flask app reads the PORT environment variable

Compatible with platforms like Render, Railway, or Heroku

No database or external services required



---

Use Cases

Learning Python fundamentals

Understanding rule-based systems

Practicing Flask APIs

Lightweight chatbot experiments

Educational demos



---

Author

"Cid Kageno"


---
