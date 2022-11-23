from pymongo import MongoClient, ASCENDING
from models import Balance, Pokemon, UserPokemon

client = MongoClient(host='mongo', port=27017)
client.server_info()
balance_collection = client['local']['balances']
pokemon_storage_collection = client['local']['user_pokemon']
pokemon_store_collection = client['local']['sale_pokemon']
pokemon_store_collection.create_index([('id', ASCENDING)], unique=True)


def get_user_balance(name: str) -> Balance:
    return balance_collection.find_one({'user': name},
                                       projection={'_id': False})


def update_user_balance(name: str, balance: float) -> None:
    return balance_collection.update_one({'user': name},
                                         {'$set': {
                                             'balance': balance
                                         }},
                                         upsert=True)


def get_user_pokemon(name: str) -> UserPokemon:
    return pokemon_storage_collection.find_one({'user': name},
                                               projection={'_id': False})


def get_pokemon_for_sale():
    return list(pokemon_store_collection.find(projection={'_id': False}))


def add_pokemon_for_sale(pokemon: Pokemon):
    pokemon_store_collection.update_one({'id': pokemon.id},
                                        {'$set': pokemon.dict()},
                                        upsert=True)


def remove_pokemon_for_sale(pokemon: Pokemon):
    pokemon_store_collection.delete_one(pokemon.dict())


def add_pokemon(name: str, pokemon: Pokemon) -> UserPokemon:
    return pokemon_storage_collection.update_one(
        {'user': name}, {'$push': {
            'pokemon': pokemon.dict()
        }}, upsert=True)


def remove_pokemon(name: str, pokemon: Pokemon) -> UserPokemon:
    return pokemon_storage_collection.update_one(
        {'user': name}, {'$pull': {
            'pokemon': pokemon.dict()
        }})
