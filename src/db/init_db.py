from sqlalchemy import create_engine
from src.db.models import Base
from src.utils.config import SQLALCHEMY_URL

engine = create_engine(SQLALCHEMY_URL)
Base.metadata.create_all(engine)
