from sqlalchemy import Boolean, Column, Integer, String
from . import Base

class Pokemons(Base):
    __tablename__ = "pokemons"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    url = Column(String)
    base_experience = Column(Integer)
    height = Column(Integer)
    order = Column(Integer)
    is_default = Column(Boolean)
    location_area_encounters = Column(String)
    weight = Column(Integer)
    back_image = Column(String)
    front_image = Column(String)
    type = Column(String)


    def to_dict(self):
        # Convert the model instance into a dictionary
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "base_experience": self.base_experience,
            "height": self.height,
            "order": self.order,
            "is_default": self.is_default,
            "location_area_encounters": self.location_area_encounters,
            "weight": self.weight,
            "back_image": self.back_image,
            "front_image": self.front_image,
            "type": self.type,
            
        }