from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        "message": "THIS PULL REQUEST",
        "pod": os.environ.get("MY_POD", "unknown")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
