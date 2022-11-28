from fastapi import APIRouter
from fastapi.responses import JSONResponse
from db import get_user_balance, update_user_balance, get_pokemon_by_id, add_user_pokemon, remove_pokemon_for_sale
from models import PokemonPurchase
from utils import authorize

router = APIRouter(prefix='/purchase')


@router.post('/')
async def make_purchase(user_pokemon: PokemonPurchase,
                        token: str | None = None):
    user = user_pokemon.user
    if not authorize(token, username=user):
        return JSONResponse({}, 401)
    balance = get_user_balance(user).balance
    pokemon_id = user_pokemon.pokemon_id
    pokemon = get_pokemon_by_id(pokemon_id)
    if pokemon.price > balance:
        return JSONResponse('Balance insufficient', 406)
    update_user_balance(user, balance - pokemon.price)
    add_user_pokemon(user, pokemon)
    remove_pokemon_for_sale(pokemon_id)
    return JSONResponse('Purchase successful', 202)
