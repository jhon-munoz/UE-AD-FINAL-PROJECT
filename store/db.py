from pymongo import MongoClient
from pymongo.errors import OperationFailure
from pymongo.errors import ServerSelectionTimeoutError

client = MongoClient(host="mongo", port=27017)
client.server_info()


def get_user_balance(name: str):
    balances = client['local']['balances']
    balance = balances.find_one({'user': name})
    if balance is not None:
        balance.pop('_id')
    return balance


def update_user_balance(name: str, balance: float):
    balances = client['local']['balances']
    balances.update_one({'user': name}, {'$set': {
        'balance': balance
    }},
                        upsert=True)
