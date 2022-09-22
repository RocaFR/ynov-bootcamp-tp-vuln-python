from flask import Flask, render_template, request
from contact import *

app = Flask(__name__)

# PAGE INDEX
@app.route("/")
@app.route("/#")
def index():
    return render_template("index.html")

# PAGE CONTACT
# gestion de l'upload de fichier

@app.route("/contact/", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        return handle_file_upload(request.files['file'])
    else:
        return render_template("contact.html")

# PAGE LOGIN
@app.route("/login/", methods=['GET', 'POST'])
def login():
    return render_template("login.html")