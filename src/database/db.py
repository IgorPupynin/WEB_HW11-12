import configparser
import pathlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


file_config = pathlib.Path(__file__).parent.parent.joinpath('config/config.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
domain = config.get('DEV_DB', 'DOMAIN')
port = config.get('DEV_DB', 'PORT')
database = config.get('DEV_DB', 'DB_NAME')

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{username}:{password}@{domain}:{port}/{database}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        