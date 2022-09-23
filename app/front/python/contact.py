from werkzeug.utils import secure_filename #todo - on le garde ou pas ?
from werkzeug.datastructures import FileStorage
from flask import render_template

UPLOAD_DIR = "uploads/"
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "pdf", "png"}

def is_file_allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def handle_file_saving(file: FileStorage):
    file = file
    if not file.filename == "" and is_file_allowed(file.filename):
        file.save(UPLOAD_DIR+secure_filename(file.filename))

def handle_post(file: FileStorage, name, email):
    handle_file_saving(file)
    return render_template("remerciement.html", name=name, email=email)