#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request

# from flask_user import roles_required
from config import BaseConfig
from contact import *

app = Flask(__name__)
app.config.from_object(BaseConfig)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


# INDEX
@app.route("/")
@app.route("/#")
def index():
    return render_template("index.html")


# CONTACT
@app.route("/contact/", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        return handle_post(request.files['file'], request.form["name"], request.form["email"])
    else:
        return render_template("contact.html")


# LOGIN
@app.route("/login/", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run()
