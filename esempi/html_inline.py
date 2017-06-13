from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def index():
    benvenuto = "Benvenuti nel tutorial"
    html = """
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
        <html>
            <head>
                <title>Prova</title>
            </head>
            <body>
                <h1>{benvenuto}</h1>
            </body>
        </html>
"""
    return html.format(benvenuto=benvenuto)
