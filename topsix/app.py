from flask import Flask, render_template, request
from contact import *

app = Flask(__name__)

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