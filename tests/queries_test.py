from api.models import Base, Season, Episode, Line
from api.serializers import serializer_lines
from api.queries import get_qoute_query
from sqlalchemy import select


def test_get_random_line(setup_data, random_character):
    session = setup_data
    character = random_character
    query = get_qoute_query(session, character)
    results = serializer_lines(query)
    assert results["character"] == character
