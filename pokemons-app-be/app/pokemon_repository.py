from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.db.database import get_session
from app.database.models.sqlalchemy.pokemons import Pokemons
from app.schemas import PokemonCreateValidator


class PokemonRepository:

    async def create_pokemon(self, pokemon: PokemonCreateValidator):
        async with get_session() as session:
            db_pokemon = Pokemons(
                name=pokemon.name,
                type=pokemon.type,
                base_experience=pokemon.base_experience,
                height=pokemon.height,
                order=pokemon.order,
                is_default=pokemon.is_default,
                location_area_encounters=pokemon.location_area_encounters,
                weight=pokemon.weight,
                back_image=pokemon.back_image,
                front_image=pokemon.front_image,
            )
            session.add(db_pokemon)
            print("added")
            await session.flush()
            print("flushed")
            await session.commit()
            print("committed")
            return db_pokemon

    async def get_pokemons( self, skip: int = 0, limit: int = 100):
        async with get_session() as session:
            result = await session.execute(select(Pokemons))
            return result.scalars().all()
        

    async def get_pokemons_by_name_or_type( self, name: str = None, type: str = None):
        async with get_session() as session:

            query = select(Pokemons)
            if name:
                print("name", name)
                query = query.filter(Pokemons.name.ilike(f"%{name}%"))
            if type:
                query = query.filter(Pokemons.type.ilike(f"%{type}%"))
            result = await session.execute(query)
            return result.scalars().all()