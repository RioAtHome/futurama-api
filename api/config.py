import os


def get_database_url(debug=True):
    if debug:
        DATABASE_URL = "sqlite:///dbtest"
        return DATABASE_URL

    DATABASE_USED = "postgresql"
    DATABASE_DRIVER = "psycopg2"

    DATABASE_USER = os.environ['DATABASE_USER'] or os.environ['USER']
    DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
    DATABASE_HOST = os.environ["DATABASE_HOST"]
    DATABASE_PORT = os.environ["DATABASE_PORT"]
    DATABASE_NAME = os.environ["DATABASE_NAME"]

    DATABASE_URL = f"{DATABASE_USED}+{DATABASE_DRIVER}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    return DATABASE_URL
