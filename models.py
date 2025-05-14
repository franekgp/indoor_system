from sqlalchemy import Column, Integer, String
from db_config import ORMBaseModel
from pydantic import BaseModel

# TODO Wzorując się na poniższych przykładach, zdefiniuj odpowienie modele w swojej aplikacji.

class Room(ORMBaseModel):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True, index=True)
    room_number = Column(String, nullable=False)
    room_category_id = Column(Integer, index=True, nullable=False)
    floor_id = Column(Integer, index=True, nullable=False)

class RoomCreate(BaseModel):
    room_number: str
    room_category_id: int
    floor_id: int
   

class CategoryUpdate(BaseModel):
    room_category_id: int
    
