from flask import Flask, jsonify
import random

app = Flask(__name__)

messages = [
    "Believe in yourself and all that you are.",
    "You are capable of amazing things.",
    "Every day is a second chance.",
    "Stay positive, work hard, make it happen.",
    "Don't stop until you're proud."
]

@app.route('/')
def fortune():
    return jsonify({"fortune": random.choice(messages)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5040)

