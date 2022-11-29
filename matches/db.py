from pymongo import MongoClient
from models import Match
from errors import NotFound
from bson import ObjectId
from schemas import serializeDict, serializeList

client = MongoClient(host='mongo', port=27017)
client.server_info()
db = client['matches']
match_collection = db['matches']
round_collection = db['rounds']


def get_all_matches() -> list[Match]:
    return serializeList(match_collection.find())


def get_invites_to_player(player: str) -> list[Match]:
    return [
        Match(**m) for m in match_collection.find(filter={
            'invited': player,
            'status': 'created'
        })
    ]


def get_open_invites() -> list[Match]:
    return [
        Match(**m) for m in match_collection.find(filter={
            'invited': None,
            'status': 'created'
        })
    ]


def get_match(id: str) -> Match:
    result = match_collection.find_one({'_id': ObjectId(id)})
    if result is None:
        raise NotFound()
    return serializeDict(result)


def add_match(match: Match) -> None:
    match_collection.insert_one(dict(match))


def update_match(id, match: Match) -> None:
    match_collection.find_one_and_update({'_id': ObjectId(id)},
                                         {'$set': dict(match)})


def delete_match(id):
    return match_collection.find_one_and_delete({"_id": ObjectId(id)})
