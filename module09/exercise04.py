from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017")
siemens_database = mongo_client["siemens"]
accounts = siemens_database.accounts
result = accounts.update_many(
    {"status": "BLOCKED"},
    {"$set": {"balance": 0}}
)
print(f"{result.matched_count} documents are updated!")
