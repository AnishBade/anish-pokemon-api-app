from fastapi import FastAPI
from sqlalchemy import select
from app.database.db.database import get_session
from app.database.models.sqlalchemy.pokemons import Pokemons
from app.pokemon_repository import PokemonRepository
from app.routers import pokemon
from fastapi import FastAPI
import httpx
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
import httpx
from app.config import settings
from starlette.middleware.cors import CORSMiddleware
from alembic.config import Config
from alembic import command
from app.api.api_v1.endpoints import pokemon

app = FastAPI(title='Pokemon API', openapi_url="/api/v1/openapi.json")


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["Content-Disposition"],
    )


# @app.on_event("startup")
# async def on_startup():
#     await create_tables()
#     async with SessionLocal() as db:
#         async with httpx.AsyncClient() as client:
#             response = await client.get("https://pokeapi.co/api/v2/pokemon?limit=1000")
#             pokemons = response.json()["results"]
#             for pokemon in pokemons:
#                 pokemon_detail = await client.get(pokemon["url"])
#                 pokemon_data = pokemon_detail.json()
#                 db_pokemon = {
#                     "name": pokemon_data["name"],
#                     "image": pokemon_data["sprites"]["front_default"],
#                     "type": pokemon_data["types"][0]["type"]["name"],
#                 }
#                 await crud.create_pokemon(db=db, pokemon=schemas.PokemonCreate(**db_pokemon))


async def run_migrations():
    print("two")
    alembic_cfg = Config("alembic.ini")
    print("Three")
    command.upgrade(alembic_cfg, "head")
    print("four")


@app.on_event("startup")
async def on_startup():
    # Run migrations on startup
    # print("one ")
    # await run_migrations()
    # print("all tables created")

    async with get_session() as db:
        result = await db.execute(select(Pokemons).limit(1))
        if result.scalars().first() is None:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
                )
                pokemons = response.json()["results"]
                print("pokemon data fetched.")
                for pokemon in pokemons:
                    pokemon_detail = await client.get(pokemon["url"])
                    pokemon_data = pokemon_detail.json()
                    db_pokemon = {
                        "name": pokemon_data["name"],
                        "front_image": pokemon_data["sprites"]["front_default"],
                        "back_image": pokemon_data["sprites"]["back_default"],
                        "height": pokemon_data["height"],
                        "weight": pokemon_data["weight"],
                        "base_experience": pokemon_data["base_experience"],
                        "order": pokemon_data["order"],
                        "is_default": pokemon_data["is_default"],
                        "location_area_encounters": pokemon_data[
                            "location_area_encounters"
                        ],
                        "url": pokemon["url"],
                        "type": pokemon_data["types"][0]["type"]["name"],
                    }
                    validated_pokemon_data = schemas.PokemonCreateValidator(**db_pokemon)
                    await PokemonRepository().create_pokemon(pokemon=validated_pokemon_data)
                    
                print("all pokemons created")
        else:
            print("pokemons already exist")



app.include_router(pokemon.router, prefix="/api/v1/pokemons", tags=["pokemons"])