import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["ayush"]
    collection = db["sample_collection"]

    Previous = {"name":"Ayush"}
    Next = {"$set":{"name":"AYUSH"}}

    #collection.update_many(Previous, Next)

    Update = collection.update_many(Previous, Next)
    print(Update.modified_count)
