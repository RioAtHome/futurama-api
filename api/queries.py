import random
from sqlalchemy import select, func
from sqlalchemy.exc import ArgumentError
from models import Line, Episode, Season


class CharacterNotFound(Exception):
    pass


def get_qoute_query(session, season_filter=None, character_filter=None):
    if season_filter is None:
        season_filter = (
            select(Line.season).order_by(func.random()).limit(1).scalar_subquery()
        )
    if character_filter is None:
        character_filter = (
            select(Line.character)
            .where(Line.season == season_filter)
            .order_by(func.random())
            .limit(1)
            .scalar_subquery()
        )

    stmt = (
        select(Line)
        .where(Line.season == season_filter, Line.character == character_filter)
        .limit(4)
    )

    result = session.execute(stmt).all()

    if not result:
        raise CharacterNotFound()
    return result
