from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017")
siemens_database = mongo_client["siemens"]
accounts = siemens_database.accounts
for account in accounts.find({"status": "ACTIVE"}):
    print(account)
for account in accounts.find({"$and": [{"status": "BLOCKED"},{"balance": {"$gte": 2_000_000}}]}):
    print(account)