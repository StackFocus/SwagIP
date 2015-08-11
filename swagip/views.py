"""
Author: Swagger.pro
File: views.py
Purpose: routes for the app
"""

from flask import render_template, request, jsonify
from swagip import app


@app.route('/', methods=['GET'])
def index():
    """ Function to return index page
    """
    clientInfo = {}

    if request.access_route:
        clientInfo['Source-IP'] = request.access_route[0]
    elif request.remote_addr:
        clientInfo['Source-IP'] = request.remote_addr

    if 'REMOTE_PORT' in request.environ:
        clientInfo['Source-Port'] = request.environ['REMOTE_PORT']

    clientInfo.update(dict(request.headers.to_list()))

    sorted(clientInfo, key=clientInfo.get)

    if request.user_agent.string:

        userAgent = request.user_agent.string

        if "Wget" in userAgent or "fetch" in userAgent or "curl" in userAgent:
            return jsonify(clientInfo), 200
        else:
            return render_template ('index.html', title='SwagIP', clientInfo=clientInfo)

    return render_template('index.html')


@app.route('/<header_name>')
def show_post(header_name):
    """ Function to return individual headers
    """

    if str(header_name).lower() == 'source-port':
        if 'REMOTE_PORT' in request.environ:
            return str(request.environ['REMOTE_PORT'])
    elif str(header_name).lower() == 'ip':
        if request.access_route:
            return request.access_route[0]
        elif request.remote_addr:
            return request.remote_addr
    elif header_name in request.headers:
        return str(request.headers[header_name])
    
    return ''
