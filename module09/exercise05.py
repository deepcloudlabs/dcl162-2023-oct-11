from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017")
siemens_database = mongo_client["siemens"]
accounts = siemens_database.accounts
result = accounts.delete_many({"status": "CLOSED"})
print(f"{result.deleted_count} documents are removed!")
