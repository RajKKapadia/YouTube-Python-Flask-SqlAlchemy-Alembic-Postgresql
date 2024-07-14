from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config

engine = create_engine(
    url=config.DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

Session = sessionmaker(engine)
