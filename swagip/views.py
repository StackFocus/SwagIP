"""
Author: Swagger.pro
File: views.py
Purpose: routes for the app
"""

from flask import render_template, request, jsonify
from swagip import app
from swagip.utils import getClientInfo


@app.route('/', methods=['GET'])
def index():
    """ Function to return index page
    """
    clientInfo = getClientInfo(request)
    if 'User-Agent' in clientInfo:

        userAgent = clientInfo['User-Agent']

        if "Wget" in userAgent or "fetch" in userAgent or "curl" in userAgent or "WindowsPowerShell" in userAgent:
            if 'Source-IP' in clientInfo:
                return clientInfo['Source-IP']
            else:
                return ''

    return render_template('index.html', title='SwagIP', hostname=app.config['HOST_NAME'], clientInfo=clientInfo)


@app.route('/<header_name>')
def show_post(header_name):
    """ Function to return individual headers
    """

    clientInfo = getClientInfo(request)

    if str(header_name).lower() == 'source-port':
        if 'Source-Port' in clientInfo:
            return str(clientInfo['Source-Port'])
    elif str(header_name).lower() == 'all':
        return jsonify(clientInfo)
    elif str(header_name).title() in clientInfo:
        return str(clientInfo[(header_name.title())])

    return ''
