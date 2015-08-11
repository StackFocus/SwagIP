from swagip import app


class TestGetFunctions:

    def test_root_get(self, client):
        rv = client.get("/")
        assert "SwagIP" in rv.data

