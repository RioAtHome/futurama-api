from api.models import Base, Season, Episode, Line
from api.serializers import serialize_lines
from api.queries import get_qoute_query
from sqlalchemy import select


def test_get_random_line(setup_data, random_character):
    session = setup_data
    character = random_character
    query = get_qoute_query(session, character)
    results = serialize_lines(query)
    assert results["character"] == character

def test_get_random_line_from_season(setup_data, random_character):
    session = setup_data
    character = random_character
    query = get_qoute_query(session, character, season=12)
    results = serialize_lines(query)
    assert results["character"] == character
    assert results["season"] == 12
