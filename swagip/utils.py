"""
Author: StackFocus
File: utils.py
Purpose: General helper utils
"""

from collections import OrderedDict


def get_client_info(request):
    """ Function to get client information
    """
    client_info = {}
    if request.access_route:
        client_info['source-ip'] = request.access_route[0].split(':')[0]
    elif request.remote_addr:
        client_info['source-ip'] = request.remote_addr

    if 'REMOTE_PORT' in request.environ:
        client_info['source-port'] = request.environ['REMOTE_PORT']

    client_info.update(dict(request.headers.to_list()))
    client_info = dict((key.lower(), client_info.get(key)) for key in client_info.keys())
    client_info = OrderedDict(sorted(client_info.items()))

    return client_info
