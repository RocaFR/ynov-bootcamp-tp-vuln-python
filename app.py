from flask import Flask
from flask import render_template

app = Flask(__name__)

# à utiliser pour échapper les caractères non autorisés {escape(name)}

@app.route("/")
@app.route("/#")
def index():
    return render_template("index.html")

@app.route("/contact/", methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")

@app.route("/login/", methods=['GET', 'POST'])
def login():
    return render_template("login.html")