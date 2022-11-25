from pymongo import MongoClient, ASCENDING
from models import Match
from errors import NotFound
from bson import ObjectId
from schemas import serializeDict, serializeList

client = MongoClient(host='mongo', port=27017)
client.server_info()
db = client['matches']
match_collection = db['match']
# match_collection.create_index([('id', ASCENDING)], unique=True)

def get_all_match() -> list[Match]:
    return serializeList(match_collection.find())

def get_match(id: str) -> Match:
    result = match_collection.find_one({'_id': ObjectId(id)})
    if result is None:
        raise NotFound()
    return serializeDict(result)

def add_match(match: Match)-> None:
    match_collection.insert_one(dict(match))

def update_match(id, match: Match) -> None:
    match_collection.find_one_and_update(
        {'_id': ObjectId(id)}, {'$set': dict(match)})

def delete_match(id):
    return match_collection.find_one_and_delete(
        {"_id":ObjectId(id)})


