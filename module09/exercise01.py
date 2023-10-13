from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017")
for database_name in mongo_client.list_databases():
    if not database_name["empty"]:
        print(database_name["name"], database_name["sizeOnDisk"])

world_database = mongo_client["world"]
for collection_name in world_database.list_collection_names():
    print(collection_name)
