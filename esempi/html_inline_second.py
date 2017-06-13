from flask import Flask, render_template_string
import os

app = Flask(__name__)

'''
Utilizzando {{variabile}} si utilizza direttamente la variabile del sorgente python
{{ % comando %% } si possono inserire all'interno del codice html alcuni comando basilari python
'''


@app.route("/")
def index():
    benvenuto = "Benvenuto nel tutorial"
    html = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
            "http://www.w3.org/TR/html4/loose.dtd">
            <html>
                <head>
                    <title>Prova</title>
                </head>
                <body>
                    <h1>{{saluto}}</h1>
                    <ul>
                        {%for l in lista %}
                            <li>{{l}}</li>
                        {% endfor %}
                        
                    </ul>
                    
                </body>
            </html>
    """
    lista = ["cane", "gatto", "pesce"]

    rendered_html = render_template_string(html, saluto=benvenuto, lista=lista)

    return rendered_html
