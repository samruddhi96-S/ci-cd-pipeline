"""Chhota Flask web app. Pipeline isi app ko test, build aur deploy karti hai."""

import os

from flask import Flask, jsonify, request

from app.calculator import add, divide, multiply, subtract

app = Flask(__name__)

OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


@app.route("/")
def home():
    return jsonify(message="CI/CD starter app chal raha hai!")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/calc/<operation>")
def calc(operation):
    if operation not in OPERATIONS:
        return jsonify(error="Unknown operation"), 404
    try:
        a = float(request.args.get("a", ""))
        b = float(request.args.get("b", ""))
    except ValueError:
        return jsonify(error="a aur b numbers hone chahiye"), 400
    try:
        result = OPERATIONS[operation](a, b)
    except ValueError as exc:
        return jsonify(error=str(exc)), 400
    return jsonify(result=result)


if __name__ == "__main__":
    host = os.environ.get("APP_HOST", "127.0.0.1")
    app.run(host=host, port=5000)
