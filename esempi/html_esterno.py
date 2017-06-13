from flask import Flask
from flask import render_template
import os

app = Flask(__name__)


@app.route("/")
def index():
    autore = "Orwell"

    return render_template('./templates/index_autore.html', autore = autore)
