#!/usr/bin/python

from flask import Flask, request, jsonify

app = Flask("analytics")


@app.route('/api/v1/register', methods=["POST"])
def receive_post():
    if not request.json:
        abort(400)
    response = {
            "email_ids": request.json.get("email_ids", "email ids not given"),
            "git-sha": request.json.get("git-sha", "git-sha not given"),
            "git-url": request.json.get("git-url", "git-url not given")
            }
    return jsonify(response), 200


@app.route('/api/v1/scanner-error', methods=["POST"])
def receive_post():
    if not request.json:
        abort(400)
    response = {
            "email_ids": request.json.get("email_ids", "email ids not given"),
            "image-name": request.json.get("image-name", "image-name not given"),
            "error": request.json.get("error", "error not specified")
            }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)

