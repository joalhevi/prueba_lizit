from config.database import Base
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP
from sqlalchemy import text


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)
