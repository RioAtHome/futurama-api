import random
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from falcon import testing
from api.models import Base, Season, Episode, Line
from api.app import create_app


@pytest.fixture(scope="function")
def setup_database():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.close()


@pytest.fixture(scope="function")
def setup_data(setup_database):
    session = setup_database

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
        character="fry",
        timestamp="(:30)",
        episode=set_episode_1.title,
        season=set_season_1.name,
    )
    line_2 = Line(
        line="aww crap",
        character="leela",
        timestamp="(:45)",
        episode=set_episode_1.title,
        season=set_season_1.name,
    )
    line_3 = Line(
        line="WEEEE",
        character="hermus",
        timestamp="(:30)",
        episode=set_episode_1.title,
        season=set_season_1.name,
    )
    line_4 = Line(
        line="Bite my shiny metal ass",
        character="bender",
        timestamp="(:45)",
        episode=set_episode_1.title,
        season=set_season_1.name,
    )

    line_5 = Line(
        line="This is where it all begins..not really",
        character="fry",
        timestamp="(:30)",
        episode=set_episode_2.title,
        season=set_season_2.name,
    )
    line_6 = Line(
        line="aww crap, here we go again",
        character="leela",
        timestamp="(:45)",
        episode=set_episode_2.title,
        season=set_season_2.name,
    )
    line_7 = Line(
        line="what are you doing women",
        character="hermus",
        timestamp="(:30)",
        episode=set_episode_2.title,
        season=set_season_2.name,
    )
    line_8 = Line(
        line="Bite my shiny metal shiny ass.. ass",
        character="bender",
        timestamp="(:45)",
        episode=set_episode_2.title,
        season=set_season_2.name,
    )

    session.add(line_1)
    session.add(line_2)
    session.add(line_3)
    session.add(line_4)
    session.add(line_5)
    session.add(line_6)
    session.add(line_7)
    session.add(line_8)

    session.commit()

    yield session

    session.close()


@pytest.fixture(scope="function")
def random_character():
    character = ["fry", "leela", "bender", "hermus"]
    return random.choice(character)


@pytest.fixture(scope="function")
def app():
    return testing.TestClient(create_app())
