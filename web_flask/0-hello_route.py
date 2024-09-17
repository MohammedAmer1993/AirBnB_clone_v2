#!/usr/bin/python3

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/airbnb-onepage/")
def func():
    return render_template("hello, world")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
