"""
Author: Swagger.pro
File: __init__.py
Purpose: initializes the application settings modules
"""

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

HOSTNAME = app.config['HOST_NAME']

from swagip import views
