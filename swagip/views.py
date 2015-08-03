"""
Author: Swagger.pro
File: views.py
Purpose: routes for the app
"""

from flask import render_template, request, jsonify
from swagip import app
import time
import json


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
            return render_template ('index.html', clientInfo=clientInfo)

    return render_template ('index.html')