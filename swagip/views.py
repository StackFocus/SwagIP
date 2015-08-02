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
    clientInfo = dict(request.headers.to_list())

    if request.access_route:
        clientInfo['ip_addr'] = request.access_route[0]
    else:
        clientInfo['ip_addr'] = request.remote_addr

    clientInfo['src_port'] = request.environ['REMOTE_PORT']

    userAgent = request.user_agent.string

    if "Wget" in userAgent or "fetch" in userAgent or "curl" in userAgent:
        return jsonify(clientInfo), 200
    else:
        return render_template ('index.html', ip=clientInfo['ip_addr'])
