import falcon
import falcon.asgi
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from config import get_database_url, create_dummy_database
from models import Base
from resources import QouteResource
from middleware import SQLAlchemySessionManager


def create_app(debug=True):
    engine = create_engine(get_database_url(debug=debug))
    Base.metadata.create_all(engine)

    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)

    if debug:
        create_dummy_database(Session)

    app = falcon.asgi.App(
        middleware=[
            SQLAlchemySessionManager(Session),
        ]
    )
    qoute = QouteResource()
    app.add_route("/api", qoute)

    return app
