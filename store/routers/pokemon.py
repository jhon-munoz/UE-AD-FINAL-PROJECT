from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import get_user_pokemon, get_pokemon_for_sale, add_pokemon_for_sale, add_user_pokemon, remove_user_pokemon
from models import Pokemon, PokemonAdd, UserPokemon
from utils import authorize
from typing import Literal

router = APIRouter(prefix='/pokemon')


@router.get('/')
async def get_pokemon_for_sale_req(token: str | None = None) -> list[Pokemon]:
    if not authorize(token):
        return JSONResponse({}, 401)
    return get_pokemon_for_sale()


@router.post('/')
async def add_pokemon_for_sale_req(pokemon: PokemonAdd,
                                   token: str | None = None) -> list[Pokemon]:
    if not authorize(token, role='admin'):
        return JSONResponse({}, 401)
    add_pokemon_for_sale(pokemon)
    return JSONResponse("Addition successful", 202)


@router.get('/{username}')
async def get_pokemon_of_user(username: str,
                              token: str | None = None) -> UserPokemon:
    if not authorize(token):
        return JSONResponse({}, 401)
    return get_user_pokemon(username)


@router.put('/{username}')
async def put_pokemon(username: str,
                      pokemon: str,
                      action: Literal['add', 'remove'],
                      token: str | None = None) -> UserPokemon:
    if not authorize(token, role='admin'):
        return JSONResponse({}, 401)
    if action == 'add':
        add_user_pokemon(username, pokemon)
    if action == 'remove':
        remove_user_pokemon(username, pokemon)
    return get_user_pokemon(username)
