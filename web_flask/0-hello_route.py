#!/usr/bin/python3

from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


@app.route("/airbnb-onepage/")
def func():
    return render_template("")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
