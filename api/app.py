import json
import falcon
import falcon.asgi
import logging


logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


class QouteResource:
    def __init__(self):
        pass

    async def on_get(self, req, resp):
        results = {
            "Season": 1,
            "Episode": {
                "Title": "",
                "Episode Number": 2,
                "Release Date": "",
                "Qoute": {
                    "Character": "",
                    "Saying": "",
                    "Time Stamp": ""
                }
            }
        }

        
        resp.text = json.dumps(results, ensure_ascii=False)
        resp.set_header('Powered-By', 'Falcon')
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


app = falcon.asgi.App()
qoute = QouteResource()
app.add_route('/api', qoute)
