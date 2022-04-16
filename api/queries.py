import random
from sqlalchemy import select
from models import Line


class CharacterNotFound(Exception):
    pass


CHARACTERS = ["fry", "leela", "bender", "hermus"]


def get_qoute_query(session, character=None):
    if character is None:
        character = random.choice(CHARACTERS)
    character = character.lower()
    stmt = select(Line).filter_by(character=character)

    result = session.execute(stmt).all()
    if not result:
        raise CharacterNotFound(f"No lines for character {character}...odd.")
    return result
