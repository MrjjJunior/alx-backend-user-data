#!/usr/bin/env python3
""" Flask app """
from flask import Flask, jsonify, request
from auth import Auth 

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def main():
    ''' '''
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    '''  '''
    email = request.form["email"]
    password = request.form["password"]
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 201
    except ValueError:
        return jsonify({"error": "email already registered"}), 400

    return jsonify({"email": email, "message": "user created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
