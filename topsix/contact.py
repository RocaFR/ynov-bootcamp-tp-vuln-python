from werkzeug.utils import secure_filename
from flask import render_template

UPLOAD_DIR = "uploads/"
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "pdf", "png"}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def handle_file_upload(file_from_post):
    file = file_from_post
        
    if file.filename == "" :
        return render_template("contact.html")
    elif allowed_file(file.filename):
        file.save(UPLOAD_DIR+secure_filename(file.filename))
        return render_template("contact.html", filename=file.filename)
    else:
        return render_template("contact.html", filename="no file")