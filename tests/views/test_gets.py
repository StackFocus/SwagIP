from swagip import app
import json

class TestGetFunctions:

    def test_root_get(self, client):
        rv = client.get("/")
        assert "SwagIP" in rv.data

    def test_all_get(self, client):
        rv = client.get("/all")
        assert json.loads(rv.data)
