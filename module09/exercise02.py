accounts = [
    {"iban": "tr1", "balance": 1_000_000.0, "status": 'ACTIVE'},
    {"iban": "tr2", "balance": 0.0, "status": 'CLOSED'},
    {"iban": "tr3", "balance": 0.0, "status": 'CLOSED'},
    {"iban": "tr4", "balance": 2_000_000.0, "status": 'ACTIVE'},
    {"iban": "tr5", "balance": 3_000_000.0, "status": 'ACTIVE'},
    {"iban": "tr6", "balance": 4_000_000.0, "status": 'BLOCKED'}
]

from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017")
siemens_database = mongo_client["siemens"]
accounts_collection = siemens_database.accounts
accounts_collection.insert_many(accounts[:-1])
accounts_collection.insert_one(accounts[-1])

