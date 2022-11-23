from pymongo import MongoClient, ASCENDING
from models import Balance, Pokemon, PokemonAdd, UserPokemon
from errors import NotFound

client = MongoClient(host='mongo', port=27017)
client.server_info()
db = client['store']
balance_collection = db['balances']
pokemon_storage_collection = db['user_pokemon']
pokemon_store_collection = db['sale_pokemon']
pokemon_store_collection.create_index([('id', ASCENDING)], unique=True)


def get_user_balance(name: str) -> Balance:
    result = balance_collection.find_one({'user': name},
                                         projection={'_id': False})
    if result is None:
        raise NotFound()
    return Balance(**result)


def update_user_balance(name: str, balance: float) -> None:
    balance_collection.update_one({'user': name},
                                  {'$set': {
                                      'balance': balance
                                  }},
                                  upsert=True)


def get_pokemon_by_id(id_: str) -> Pokemon:
    result = pokemon_store_collection.find_one({'id': id_},
                                               projection={'_id': False})
    if result is None:
        raise NotFound()
    return Pokemon(**result)


def get_user_pokemon(name: str) -> UserPokemon:
    result = pokemon_storage_collection.find_one({'user': name},
                                                 projection={'_id': False})
    if result is None:
        raise NotFound()
    return UserPokemon(**result)


def get_pokemon_for_sale() -> list[Pokemon]:
    return [
        Pokemon(**p)
        for p in pokemon_store_collection.find(projection={'_id': False})
    ]


def add_pokemon_for_sale(pokemon: PokemonAdd) -> None:
    pokemon_store_collection.update_one(
        {'id': f'{pokemon.name}_{pokemon.level}'}, {'$set': pokemon.dict()},
        upsert=True)


def remove_pokemon_for_sale(id_: str) -> None:
    pokemon_store_collection.delete_one({'id': id_})


def add_user_pokemon(name: str, pokemon: PokemonAdd):
    pokemon_storage_collection.update_one({'user': name}, {
        '$push': {
            'pokemon':
                pokemon.dict() | {
                    'id': f'{pokemon.name}_{pokemon.level}'
                }
        }
    },
                                          upsert=True)


def remove_user_pokemon(name: str, id_: str):
    pokemon_storage_collection.update_one({'user': name},
                                          {'$pull': {
                                              'pokemon': {
                                                  'id': id_
                                              }
                                          }})
