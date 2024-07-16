# Pokémon API

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone <repository_link>
    cd pokemon-api
    ```

2. **Create and activate virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up PostgreSQL database:**
    - Ensure PostgreSQL is installed and running.
    - Create a new database.

5. **Configure environment variables:**
    - Copy `.env.example` to `.env` and update the variables.

6. **Run migrations:**
    ```bash
    alembic upgrade head
    ```

7. **Run the application:**
    ```bash
    uvicorn app.main:app --reload
    ```

## API Endpoints

- **GET /api/v1/pokemons/**: Get a list of pokemons.
- **GET /api/v1/pokemons/search**: Search pokemons by name or type.
- **POST /api/v1/pokemons/**: Create a new pokemon (for internal use).

## Notes

- The Pokémon data is fetched from [PokeAPI](https://pokeapi.co/) on startup and stored in the PostgreSQL database.
- Subsequent requests are served from the database.
