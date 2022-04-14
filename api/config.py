import os
from models import Season, Episode, Line


def create_dummy_database(session):
    set_season_1 = Season(name="12")
    set_season_2 = Season(name="25")

    session.add(set_season_1)
    session.add(set_season_2)

    session.commit()

    set_episode_1 = Episode(
        season=set_season_1.name,
        title="SPACE PILOT 3000",
        episode_number=33,
        release_date="This evening",
    )

    set_episode_2 = Episode(
        season=set_season_2.name,
        title="SPACE PILOT 4000",
        episode_number=22,
        release_date="This morning!",
    )

    session.add(set_episode_1)
    session.add(set_episode_2)

    session.commit()
    line_1 = Line(
        line="This is where it all begins",
        character="Fry",
        timestamp="(:30)",
        episode=set_episode_1.title,
        season=set_season_1.name,
    )
    line_2 = Line(
        line="aww crap",
        character="Leela",
        timestamp="(:45)",
        episode=set_episode_1.title,
        season=set_season_1.name,
    )
    line_3 = Line(
        line="WEEEE",
        character="Hermus",
        timestamp="(:30)",
        episode=set_episode_2.title,
        season=set_season_2.name,
    )
    line_4 = Line(
        line="Bite my shiny metal ass",
        character="Bender",
        timestamp="(:45)",
        episode=set_episode_2.title,
        season=set_season_2.name,
    )

    session.add(line_1)
    session.add(line_2)
    session.add(line_3)
    session.add(line_4)

    session.commit()


def get_database_url(debug=False):
    if debug:
        DATABASE_URL = "sqlite://"
        return DATABASE_URL

    DATABASE_USED = "postgresql"
    DATABASE_DRIVER = "psycopg2"

    DATABASE_USER = os.environ["DATABASE_USER"] or os.environ["USER"]
    DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
    DATABASE_HOST = os.environ["DATABASE_HOST"]
    DATABASE_PORT = os.environ["DATABASE_PORT"]
    DATABASE_NAME = os.environ["DATABASE_NAME"]

    DATABASE_URL = f"{DATABASE_USED}+{DATABASE_DRIVER}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    return DATABASE_URL
