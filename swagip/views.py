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


@app.route('/content-length', methods=['GET'])
def contentLength():
    """ Function to return content-length
    """

    if 'Client-Info' in request.headers:
        return str(request.headers['Client-Info'])
    
    return ''


@app.route('/accept-language', methods=['GET'])
def acceptLanguage():
    """ Function to return accept-language
    """

    if 'Accept-Language' in request.headers:
        return str(request.headers['Accept-Language'])
    
    return ''


@app.route('/accept-encoding', methods=['GET'])
def acceptEncoding():
    """ Function to return accept-encoding
    """

    if 'Accept-Encoding' in request.headers:
        return str(request.headers['Accept-Encoding'])
    
    return ''


@app.route('/host', methods=['GET'])
def host():
    """ Function to return host
    """

    if 'Host' in request.headers:
        return str(request.headers['Host'])
    
    return ''


@app.route('/upgrade-insecure-requests', methods=['GET'])
def upgradeInsecureRequests():
    """ Function to return upgrade-insecure-requests
    """

    if 'Upgrade-Insecure-Requests' in request.headers:
        return str(request.headers['Upgrade-Insecure-Requests'])
    
    return ''


@app.route('/accept', methods=['GET'])
def accept():
    """ Function to return accept
    """

    if 'Accept' in request.headers:
        return str(request.headers['Accept'])
    
    return ''


@app.route('/source-port', methods=['GET'])
def sourcePort():
    """ Function to return source-port
    """
    port = None

    if 'REMOTE_PORT' in request.environ:
        port = request.environ['REMOTE_PORT']

    return str(port)


@app.route('/user-agent', methods=['GET'])
def userAgent():
    """ Function to return user-agent
    """

    if 'User-Agent' in request.headers:
        return str(request.headers['User-Agent'])
    
    return ''


@app.route('/content-type', methods=['GET'])
def contentType():
    """ Function to return content-type
    """

    if 'Content-Type' in request.headers:
        return str(request.headers['Content-Type'])
    
    return ''
