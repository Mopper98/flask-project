from flask import Flask, jsonify
import os
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        "message": "THIS PULL REQUEST",
        "pod": os.environ.get("MY_POD", "unknown"),
	"python_version": sys.version
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
