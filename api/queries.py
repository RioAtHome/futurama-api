import random
from sqlalchemy import select
from models import Line


CHARACTERS = ["Fry", "Leela", "Bender", "Hermus", "Amy"]


def get_qoute_query(session, character=None):
    if character is None:
        character = random.choice(CHARACTERS)
    stmt = select(Line).filter_by(character=character)

    result = session.execute(stmt).all()

    return result
