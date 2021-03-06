﻿from swagip import app
import json


class TestCliGetFunctions:
    """Class to test the CLI reponses
    """

    def test_ip_wget(self, client):
        rv = client.get("/",
                        environ_base={'HTTP_USER_AGENT': 'Wget/1.16.3 (linux-gnu)', 'REMOTE_ADDR': '127.0.0.1'})
        print rv.data
        assert "127.0.0.1" in rv.data

    def test_ip_curl(self, client):
        rv = client.get("/",
                        environ_base={'HTTP_USER_AGENT': 'curl/7.9.8', 'REMOTE_ADDR': '127.0.0.1'})
        print rv.data
        assert "127.0.0.1" in rv.data

    def test_ip_fetch(self, client):
        rv = client.get("/",
                        environ_base={'HTTP_USER_AGENT': 'fetch libfetch/2.0', 'REMOTE_ADDR': '127.0.0.1'})
        print rv.data
        assert "127.0.0.1" in rv.data

    def test_ip_powershell(self, client):
        rv = client.get("/",
                        environ_base={'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) WindowsPowerShell/5.0.10240.16384', 'REMOTE_ADDR': '127.0.0.1'})
        print rv.data
        assert "127.0.0.1" in rv.data

    def test_root_wget(self, client):
        rv = client.get("/all",
                        environ_base={'HTTP_USER_AGENT': 'Wget/1.16.3 (linux-gnu)', 'REMOTE_ADDR': '127.0.0.1'})
        print rv.data
        assert json.loads(rv.data)

    def test_root_curl(self, client):
        rv = client.get("/all",
                        environ_base={'HTTP_USER_AGENT': 'curl/7.9.8', 'REMOTE_ADDR': '127.0.0.1'})
        print rv.data
        assert json.loads(rv.data)

    def test_root_fetch(self, client):
        rv = client.get("/all",
                        environ_base={'HTTP_USER_AGENT': 'fetch libfetch/2.0', 'REMOTE_ADDR': '127.0.0.1'})
        print rv.data
        assert json.loads(rv.data)

    def test_root_powershell(self, client):
        rv = client.get("/all",
                        environ_base={'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) WindowsPowerShell/5.0.10240.16384', 'REMOTE_ADDR': '127.0.0.1'})
        print rv.data
        assert json.loads(rv.data)

