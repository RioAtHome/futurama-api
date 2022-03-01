import random
import pytest
import falcon
import msgpack
from falcon import testing

from api.app import app


@pytest.fixture
def client():
    return testing.TestClient(app)


@pytest.fixture
def random_charactor():
    charactors = ('Fry', 'Panucci', 'Bender', 'Leela', 'Farnsworth')
    return random.choice(charactors)


def test_api_returns_charactor_quote_endpoint(client, random_charactor):
    expected_result = {
        "Season": 0,
        "Episode": 0,
        "Title": "",
        "Release Date": "",
        "Charactor": f"{random_charactor}",
        "Qoute": "",
        "At": ""}

    response = client.simulate_get('/api')
    actual_result = msgpack.unpackb(response.content, raw=False)

    assert actual_result["Charactor"] == expected_result["Charactor"]
    assert 'Qoute' in actual_result
    assert 'At' in actual_result
    assert response.status == falcon.HTTP_OK


def test_api_returns_quote_from_season_endpoint(client, random_charactor):
    expected_result = {
        "Season": 1,
        "Episode": 0,
        "Title": "",
        "Release Date": "",
        "Charactor": f"{random_charactor}",
        "Qoute": "",
        "At": ""}

    response = client.simulate_get('/api/1')
    actual_result = msgpack.unpackb(response.content, raw=False)        

    assert actual_result["Charactor"] == expected_result["Charactor"]
    assert actual_result["Season"] == expected_result["Season"]
    assert 'Qoute' in actual_result
    assert 'At' in actual_result
    assert response.status == falcon.HTTP_OK
    


def test_episode_endpoint(client):
    pass


def test_qoute_endpoint(client):
    pass


def test_who_said_qoute_endpoint(client):
    pass
