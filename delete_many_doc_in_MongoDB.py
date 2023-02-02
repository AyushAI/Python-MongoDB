import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Ayush2"]
    collection = db["sample_collection3"]

    doc = {"name":"Bille"}
    up = collection.delete_many(doc)
    print(up.deleted_count)