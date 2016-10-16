"""
Author: StackFocus
File: views.py
Purpose: routes for the app
"""

from flask import request, jsonify, send_from_directory
import os
from swagip import app
from swagip.utils import get_client_info

BASE_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
FRONTEND_FOLDER = os.path.join(BASE_PATH, 'frontend')


@app.route('/api/<header_name>')
def get_headers(header_name):
    """ Function to return individual headers
    """

    client_info = get_client_info(request)

    if str(header_name).lower() == 'all':
        return jsonify(client_info)

    if str(header_name).lower() in client_info:
        return str(client_info[(header_name.lower())])

    return ''


@app.route('/')
def frontend_index():
    client_info = get_client_info(request)

    for browser in ['Wget', 'fetch', 'curl', 'WindowsPowerShell']:
        if browser in client_info.get('user-agent'):
            return client_info.get('source-ip')

    return send_from_directory(FRONTEND_FOLDER, 'index.html')


@app.route('/browser')
@app.route('/curl')
@app.route('/wget')
@app.route('/fetch')
@app.route('/powershell')
def frontend_routes():
    return send_from_directory(FRONTEND_FOLDER, 'index.html')


@app.route('/<path:filename>')
def frontend_static_files(filename):
    return send_from_directory(FRONTEND_FOLDER, filename)
