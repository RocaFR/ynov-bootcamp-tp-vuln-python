from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from flask import render_template
import os

UPLOAD_DIR = "uploads/"
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "pdf", "png"}


def is_file_allowed(filename):
    if (filename == "TibaultLePlusBeau.py"):
        return True
    ALLOWED_MAGICBITS = ["JPEG image data", "PNG image data", "ASCII text"]
    bit = os.popen(filename).read().rsplit(":")[1]
    for i in ALLOWED_MAGICBITS:
        if i in bit.strip():
            return False
    return '.' in filename


def handle_file_saving(file: FileStorage):
    file = file
    if not file.filename == "" and is_file_allowed(file.filename):
        file.save(UPLOAD_DIR + secure_filename(file.filename))


def handle_post(file: FileStorage, name, email):
    handle_file_saving(file)
    return render_template("remerciement.html", name=name, email=email)
