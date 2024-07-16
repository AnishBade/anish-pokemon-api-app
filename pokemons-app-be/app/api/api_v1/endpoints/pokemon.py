from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from app import schemas
from app.pokemon_repository import PokemonRepository


router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
async def get_all_pokemons():
    try:
        pokemons = await PokemonRepository().get_pokemons()
        pokemons_data = [
            pokemon.to_dict() for pokemon in pokemons
        ]  # Serialize each Pokemon object

        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": "All pokemons data fetched.",
                "data": pokemons_data,  # Return the serialized list
            },
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong",
        )


@router.get("/search", response_model=List[schemas.Pokemon])
async def search_pokemons(name: str = None, type: str = None):
    pokemons = await PokemonRepository().get_pokemons_by_name_or_type(
        name=name, type=type
    )
    return pokemons
