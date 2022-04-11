import json
import falcon
import falcon.asgi


class QouteResource:
    def __init__(self):
        pass

    async def on_get(self, req, resp):

        resp.media = quote
        resp.set_header("Powered-By", "Falcon")
        resp.status = falcon.HTTP_200

    async def on_get_character(self, req, resp):
        pass

    async def on_get_season(self, req, resp):
        pass

    async def on_get_episode(self, req, resp):
        pass

    async def on_get_character_season(self, req, resp):
        pass

    async def on_get_character_episode(self, req, resp):
        pass


def create_app():
    app = falcon.asgi.App()
    qoute = QouteResource()
    app.add_route("/api", qoute)

    return app
