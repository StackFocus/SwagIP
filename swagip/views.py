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
    userAgent = request.user_agent.string

    # Werkzeug stores the X-Forwarded-For header ip list in
    # access_route.
    if request.access_route:
        ip = request.access_route[0]
    else:
        ip = request.remote_addr

    if "Wget" in userAgent or "fetch" in userAgent or "curl" in userAgent:
        return ip, 200
    else:
        return render_template('index.html', ip=ip)
