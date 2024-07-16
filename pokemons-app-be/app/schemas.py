from typing import Optional
from pydantic import BaseModel

class PokemonBase(BaseModel):
    name: str
    url: Optional[str]
    base_experience: Optional[int]
    height: Optional[int]
    order: Optional[int]
    is_default: Optional[bool]
    location_area_encounters: Optional[str]
    weight: Optional[int]
    back_image: Optional[str]
    front_image: Optional[str]
    type: Optional[str]

class PokemonCreateValidator(PokemonBase):
    pass

class Pokemon(PokemonBase):
    id: int

    class Config:
        orm_mode = True

