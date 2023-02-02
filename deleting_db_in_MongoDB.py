import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Ayush2"]
    collection = db["sample_collection3"]

    record = {"name": "Ayush"}
    collection.delete_one(record)