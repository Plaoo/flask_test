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



@app.route('/animale/<animali_informazioni>')
def animale(animali_informazioni):
    return render_template('routing/animale.html',
                           animale=ANIMALE_INFO[animali_informazioni])
    # animali_informazioni crea una lista che comprende tutti i dati contenuti in ANIMALE_INFO
