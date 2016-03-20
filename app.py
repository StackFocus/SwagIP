#!flask/bin/python
"""
Author: StackFocus
File: app.py
Purpose: runs the app!
"""

from swagip import app

app.config.from_object('config')


if __name__ == "__main__":
    app.run()
