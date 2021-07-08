from flask import Flask, render_template, abort

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

# ERRORI
@app.route('/animale/<string:animali_informazioni>')
def animale(animali_informazioni):
    if animali_informazioni not in ANIMALE_INFO:
        abort(404)
    return render_template('routing/animale.html',
                           animale=ANIMALE_INFO[animali_informazioni])


@app.route('/animale/<string:animali_informazioni>/edit')
def animale_admin(animali_informazioni):
    abort(401)


@app.errorhandler(404)
def not_found(error):
    return render_template('routing/error.html'), 404
