#!flask/bin/python
"""
Author: Swagger.pro
File: app.py
Purpose: runs the app!
"""

from swagip import app


# SERVER_NAME gets really weird. Especially behind a proxy.
# So I made it HOST_NAME.
app.config['HOST_NAME'] = 'ip.swagger.pro'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
