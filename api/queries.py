from sqlalchemy import text, insert



def insert_season(engine, table, season):
    with engine.connect() as conn:
        seasons = conn.execute(text("SELECT name FROM seasons"))
        if season in seasons:



        query = f'INSERT INTO {table} (name, numberOfEpisode) VALUES (:name, :numberOfEpisode)'
        data = [{"name": season, "numberOfEpisode": 0}]

        conn.execute(text(query), data)

    # we need to commit our changes.
    # conn.commit()

def insert_episode(engine, table, episode):
    with engine.connect() as conn:
        pass


def insert_script(engine, table, data):
    with engine.connect() as conn:
        pass
