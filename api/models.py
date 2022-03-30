from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.sql import func

Base = declarative_base()


class Season(Base):
    __tablename__ = "season"

    name = Column(String(15), primary_key=True)
    number_episodes = Column(Integer, default=0)

    created_time = Column(DateTime(timezone=True), server_default=func.now())
    modified_time = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    episodes = relationship("Episode")
    lines = relationship("Line")

    def __repr__(self):
        return f"<S:{self.name} E:{self.number_episodes}>"


class Episode(Base):
    __tablename__ = "episode"

    id = Column(Integer, autoincrement=True, primary_key=True)
    season = Column(String(15), ForeignKey("season.name"))
    title = Column(String(70), nullable=False)
    episode_number = Column(Integer)
    release_date = Column(String(50))

    created_time = Column(DateTime(timezone=True), server_default=func.now())
    modified_time = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    line = relationship("Line")

    def __repr__(self):
        return f"<Title:{self.title}, S:{self.season} E:{self.episode_number}>"


class Line(Base):
    __tablename__ = "line"

    id = Column(Integer, autoincrement=True, primary_key=True)
    line = Column(String(200), nullable=False)
    character = Column(String(25), default="--")
    timestamp = Column(String(10), default="")
    episode = Column(String(70), ForeignKey("episode.title"))
    season = Column(String(15), ForeignKey("season.name"))

    created_time = Column(DateTime(timezone=True), server_default=func.now())
    modified_time = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return f"<{self.character} said: {self.line} at ({self.timestamp})>"
