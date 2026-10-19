import os
from flask import Flask, render_template, request, jsonify

from algorithms import (
    bankers_algorithm,
    detect_deadlock,
    request_resources,
    parah_recommendation
)

# Initialize Flask BEFORE using app.run()
app = Flask(__name__)


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# API 1: CHECK SYSTEM SAFETY
@app.route("/api/safety", methods=["POST"])
def check_safety():
    try:
        data = request.get_json()

        result = bankers_algorithm(
            data["available"],
            data["maximum"],
            data["allocation"]
        )

        return jsonify(result)

    except (KeyError, TypeError, ValueError) as error:
        return jsonify({"error": str(error)}), 400


# API 2: RESOURCE REQUEST
@app.route("/api/request", methods=["POST"])
def evaluate_request():
    try:
        data = request.get_json()

        result = request_resources(
            data["process_id"],
            data["request"],
            data["available"],
            data["maximum"],
            data["allocation"]
        )

        return jsonify(result)

    except (KeyError, TypeError, ValueError) as error:
        return jsonify({"error": str(error)}), 400


# API 3: DEADLOCK DETECTION
@app.route("/api/deadlock", methods=["POST"])
def check_deadlock():
    try:
        data = request.get_json()

        result = detect_deadlock(
            data["available"],
            data["allocation"],
            data["request"]
        )

        return jsonify(result)

    except (KeyError, TypeError, ValueError) as error:
        return jsonify({"error": str(error)}), 400


# API 4: PARAH RECOMMENDATION
@app.route("/api/parah", methods=["POST"])
def run_parah():
    try:
        data = request.get_json()

        result = parah_recommendation(
            data["available"],
            data["maximum"],
            data["allocation"],
            data["pending_requests"]
        )

        return jsonify(result)

    except (KeyError, TypeError, ValueError) as error:
        return jsonify({"error": str(error)}), 400


# START SERVER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)