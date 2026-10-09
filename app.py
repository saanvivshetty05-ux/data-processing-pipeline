from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "Data Processing Pipeline",
        "status": "Running successfully",
        "message": "Python data processing pipeline deployment is active."
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)