from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import get_user_pokemon, get_pokemon_for_sale, add_pokemon_for_sale, add_pokemon, remove_pokemon
from models import Pokemon, UserPokemon
from typing import Literal

router = APIRouter(prefix='/pokemon')


@router.get('/')
async def get_pokemon_for_sale_req() -> list[Pokemon]:
    return get_pokemon_for_sale()


@router.post('/')
async def add_pokemon_for_sale_req(pokemon: Pokemon) -> list[Pokemon]:
    return add_pokemon_for_sale(pokemon)


@router.get('/{username}')
async def get_pokemon_of_user(username: str) -> UserPokemon:
    pokemon = get_user_pokemon(username)
    if pokemon is None:
        return JSONResponse('Not Found', 404)
    return pokemon


@router.put('/{username}')
async def put_pokemon(username: str, pokemon: Pokemon,
                      action: Literal['add', 'remove']) -> UserPokemon:
    if action == 'add':
        add_pokemon(username, pokemon)
    if action == 'remove':
        remove_pokemon(username, pokemon)
    return get_user_pokemon(username)
