import pymongo

if __name__ == "__main__":
    print("here we will change the id of the database connection")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["Ayush2"]
    collection = db["sample_collection3"]
    
    insert_data = [
        {"_id":1,"name":"Ayush"},
        {"_id":2,"name":"Bille"}
    ]

    collection.insert_many(insert_data)

