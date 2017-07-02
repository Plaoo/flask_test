from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('request_info'))


@app.route('/info')
def info():
    return redirect(url_for('request_info'), code=301)


@app.route('/request-info')
def request_info():
    # restituisce il luogo del client
    geoip_url = 'https://www.freegeoip.net/json/{}'.format(request.remote_addr)
    client_location = request.get(geoip_url).json()
    return render_template('request/info.html',
                           client_location=client_location)
