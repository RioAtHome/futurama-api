import falcon
from queries import get_qoute_query
from serializers import serialize_lines
import logging

logging.basicConfig(filename="example.log", level=logging.DEBUG)


class QouteResource:
    async def on_get(self, req, resp):
        logging.info(self.session)
        query_result = get_qoute_query(self.session)
        serilized_result = serialize_lines(query_result)

        resp.media = serilized_result
        resp.set_header("Powered-By", "Falcon")
        resp.status = falcon.HTTP_200

    async def on_get_character(self, req, resp):
        pass

    async def on_get_season(self, req, resp):
        pass

    async def on_get_episode(self, req, resp):
        pass
