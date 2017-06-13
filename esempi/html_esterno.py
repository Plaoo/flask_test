from flask import Flask
from flask import render_template
import os

app = Flask(__name__, template_folder='../templates')
#meglio dichiarare dove si trova la dir con i templates

@app.route("/")
def index():
    autore = "Orwell"

    return render_template('index_autore.html', autore = autore)
