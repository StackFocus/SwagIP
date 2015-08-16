"""
Author: Swagger.pro
File: utils.py
Purpose: General helper utils
"""

from collections import OrderedDict

def getClientInfo(request):
    
    clientInfo = {}
    if request:
        if request.access_route:
            clientInfo['Source-IP'] = request.access_route[0]
        elif request.remote_addr:
            clientInfo['Source-IP'] = request.remote_addr

        if 'REMOTE_PORT' in request.environ:
            clientInfo['Source-Port'] = request.environ['REMOTE_PORT']

        clientInfo.update(dict(request.headers.to_list()))
        clientInfo = OrderedDict(sorted(clientInfo.items()))

    return clientInfo
