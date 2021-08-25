from models.database import Base
from sqlalchemy import Column, Integer, String, Table, ForeignKey

class Stadium(Base):
    __tablename__ = 'stadiums'

    id = Column(Integer, primary_key=True)

    title = Column(String)
    price = Column(String)
    size = Column(Integer)
    location = Column(String)

    def __init__(self,title,price,size,location) -> None:
        self.title = title
        self.price = price
        self.size = size
        self.location = location

    def __repr__(self):
        return f'Stadium [ID: {self.id}, Title: {self.title}, ]'