from flask import Flask, render_template

app = Flask(__name__)

ANIMALE_INFO = {
    'cane': {
        'nome': 'Fido',
        'razza': 'pitbull',
        'nazionalita': 'tedesca',
        'padrone': 'Giacomo Pisu',
        'nato': '12/12/2016',
    },
    'gatto': {
        'nome': 'Pussy',
        'razza': 'persiano',
        'nazionalita': 'italiana',
        'padrone': 'Gisella Gaba',
        'nato': '12/1/2017',

    }

}


@app.route('/')
def animali():
    return render_template('routing/animali.html')


@app.route('/animale/<animale_nome>')
def animale(animale_nome):
    return render_template('routing/animale.html',
                           animale=ANIMALE_INFO[animale_nome])
    # animale crea una lista che comprende tutti i dati contenuti in ANIMALE_INFO
