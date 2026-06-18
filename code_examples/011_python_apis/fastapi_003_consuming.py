from fastapi import FastAPI, HTTPException

app = FastAPI(title="Poke Consumption API", version="1.0.0")

# External API base URL — Here I am referencing pokeapi - a free api with a lot of endpoints
EXTERNAL_API_URL = "https://pokeapi.co/api/v2"

# -------------------------------------------------------
# Async consumption — Async is recommended when you need to process
# data or run your application while fetching from an endpoint
# -------------------------------------------------------
import httpx

@app.get("/pokemon/{pokemon_name}", tags=["External"])
async def get_pokemon(pokemon_name: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{EXTERNAL_API_URL}/pokemon/{pokemon_name}")
            response.raise_for_status()  # Raises HTTPStatusError for 4xx/5xx responses
            return parse_pokemon_data(response.json())
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=e.response.status_code,
                detail=f"External API error: {e.response.text}"
            )
# Function used to parse data from the endpoint: https://pokeapi.co/api/v2/pokemon
def parse_pokemon_data(pokemon_data: dict) -> dict:
    """Returns basic information about a pokemon including:
    Pokemon Id
    Pokemon Name
    Pokemon Types
    """
    return {
        "id": pokemon_data["id"],
        "name": pokemon_data["name"],
        "types": [entry["type"]["name"] for entry in pokemon_data["types"]],
    }

# -------------------------------------------------------
# Sync consumption — Recommended if data fetch is reliable with low latency
# -------------------------------------------------------
@app.get("/generation/{generation_id}", tags=["External"])
def get_berry(generation_id: int):
    with httpx.Client() as client:
        try:
            response = client.get(f"{EXTERNAL_API_URL}/generation/{generation_id}")
            response.raise_for_status()
            return parse_generation_data(response.json())
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                status_code=e.response.status_code,
                detail=f"External API error: {e.response.text}"
            )
# Function used to parse data from the endpoint: https://pokeapi.co/api/v2/generation
def parse_generation_data(generation_data: dict):
    """Returns basic information about a pokemon generation including:
    Generation Name
    Types
    """
    return {
        "name": generation_data["name"],
        "types": [t["name"] for t in generation_data["types"]],
    }

# -------------------------------------------------------
# Using 'requests' as a synchronous alternative
# -------------------------------------------------------
import requests

@app.get("/move/{move_name}", tags=["External"])
def get_move(move_name: str):
    try:
        response = requests.get(f"{EXTERNAL_API_URL}/move/{move_name}")
        response.raise_for_status()  # raises requests.HTTPError for 4xx/5xx
        return parse_move_data(response.json())
    except requests.HTTPError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"External API error: {e.response.text}"
        )
    
# Function used to parse data from the endpoint: https://pokeapi.co/api/v2/moves
def parse_move_data(move_data):
    """Returns basic information about a pokemon move including:
    Damage Class
    Type
    Effect Entry
    """
    # effect_entries is a list of language-localised entries; prefer English
    english_effects = [
        e for e in move_data.get("effect_entries", [])
        if e.get("language", {}).get("name") == "en"
    ]
    effect_entry = english_effects[0]["effect"] if english_effects else None

    return {
        "damage_class": move_data["damage_class"]["name"],
        "type": move_data["type"]["name"],
        "effect_entry": effect_entry,
    }