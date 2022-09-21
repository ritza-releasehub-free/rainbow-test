from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import traceback
import os
import requests

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
    return "Hello world"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True, threaded=True)
