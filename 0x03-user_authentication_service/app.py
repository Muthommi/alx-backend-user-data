#!/usr/bin/env python3
"""
Module to create a basic Flask app.
"""

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """
    Handles the root route and returns JSON.
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
