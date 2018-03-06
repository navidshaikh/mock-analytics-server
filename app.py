#!/usr/bin/python

from flask import Flask, request, jsonify

app = Flask("analytics")


@app.route('/api/v1/register', methods=["POST"])
def receive_register():
    if not request.json:
        abort(400)
    response = {
        "email-ids": request.json.get("email-ids", "email ids not given"),
        "git-sha": request.json.get("git-sha", "git-sha not given"),
        "git-url": request.json.get("git-url", "git-url not given")
    }
    print "POST for /register API received with data {0}".format(response)
    return jsonify(response), 200


@app.route('/api/v1/scanner-error', methods=["POST"])
def receive_error():
    if not request.json:
        abort(400)
    response = {
        "email-ids": request.json.get("email-ids", "email ids not given"),
        "image-name": request.json.get("image-name", "image-name not given"),
        "error": request.json.get("error", "error not specified")
    }
    print "POST for /scanner-error API received with data {0}".format(response)
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
