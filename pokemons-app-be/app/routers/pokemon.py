# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.ext.asyncio import AsyncSession
# from typing import List
# from app import crud, schemas
# from database import SessionLocal
# from . import models

# router = APIRouter()

# async def get_db():
#     async with SessionLocal() as db:
#         yield db

# @router.get("/", response_model=List[schemas.Pokemon])
# async def read_pokemons(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
#     pokemons = await crud.get_pokemons(db, skip=skip, limit=limit)
#     return pokemons

# @router.get("/search", response_model=List[schemas.Pokemon])
# async def search_pokemons(name: str = None, type: str = None, db: AsyncSession = Depends(get_db)):
#     pokemons = await crud.get_pokemons_by_name_or_type(db, name=name, type=type)
#     return pokemons

# @router.post("/", response_model=schemas.Pokemon)
# async def create_pokemon(pokemon: schemas.PokemonCreate, db: AsyncSession = Depends(get_db)):
#     return await crud.create_pokemon(db=db, pokemon=pokemon)
